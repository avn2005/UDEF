import json
from html import escape

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse

from app.services.extraction_service import ExtractionService

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Universal Document Extraction Framework API",
        "health": "/health",
        "upload": "/upload",
        "upload_page": "/upload-page",
    }


@router.get("/upload-page", response_class=HTMLResponse)
def upload_page():
    return HTMLResponse(content="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Upload Document</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            form { max-width: 420px; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }
            input[type=file] { margin-bottom: 12px; }
            button { padding: 8px 14px; }
            pre { background: #f6f6f6; padding: 12px; border-radius: 6px; overflow-x: auto; }
        </style>
    </head>
    <body>
        <h2>Upload a document image</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <br>
            <button type="submit">Upload</button>
        </form>
        <p>Use this page to upload a JPG, JPEG, or PNG file.</p>
    </body>
    </html>
    """)


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/upload", response_class=HTMLResponse)
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    result = ExtractionService.extract(content)
    payload = {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "result": result,
    }

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Upload Result</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            pre {{ background: #f6f6f6; padding: 12px; border-radius: 6px; overflow-x: auto; }}
        </style>
    </head>
    <body>
        <h2>Upload Result</h2>
        <p>File uploaded successfully.</p>
        <pre>{escape(json.dumps(payload, indent=2))}</pre>
        <p><a href="/upload-page">Upload another file</a></p>
    </body>
    </html>
    """
    return HTMLResponse(content=html)