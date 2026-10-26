from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import sys

from app.api.routes import router

app = FastAPI(
    title="Universal Document Extraction Framework API",
    version="1.0",
    description="REST API for OCR, Extraction, Validation and Benchmark",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Router
app.include_router(router)

# Determine the frontend path
frontend_path = os.path.join(os.path.dirname(__file__), "..", "Frontend")
print(f"🔍 Looking for frontend at: {frontend_path}")

# Serve static files if the directory exists
if os.path.isdir(frontend_path):
    print(f"✅ Serving frontend from: {frontend_path}")
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
else:
    print(f"❌ Frontend directory not found: {frontend_path}")
    
    # Fallback: serve index.html directly if it exists
    index_path = os.path.join(frontend_path, "index.html")
    if os.path.isfile(index_path):
        @app.get("/")
        async def serve_index():
            return FileResponse(index_path)

# Health Check
@app.get("/health")
async def health_check():
    return {
        "success": True,
        "message": "Universal Document Extraction Framework API is running",
        "frontend_path": frontend_path,
        "frontend_exists": os.path.exists(frontend_path)
    }

