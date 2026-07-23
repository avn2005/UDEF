from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/ocr")
async def perform_ocr(file: UploadFile = File(...)):
    text = "Sample OCR Output"
    return {
        "status": "success",
        "text": text
    }
  ## replace 
  
text = extract_text(file)
