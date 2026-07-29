from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

from app.services.extraction_service import ExtractionService

# Create router
router = APIRouter()


@router.post("/upload", summary="Upload and extract document details")
async def upload_file(
    file: UploadFile = File(...),
    document_type: str = Form("auto"),
):
    try:
        # Read uploaded file
        content = await file.read()

        # Run extraction
        result = ExtractionService.extract(content, document_type)

        # Handle empty result
        if not result:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "No data extracted"
                }
            )

        # Extract only useful fields
        if isinstance(result, dict):
            data = (
                result.get("extracted_data")
                or result.get("fields")
                or result.get("data")
                or result
            )
        else:
            data = result

        # Return clean JSON for Swagger
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "document_type": document_type,
                "data": data
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e)
            }
        )