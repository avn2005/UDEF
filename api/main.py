from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Universal Document Extraction Framework API",
    version="1.0",
    description="REST API for OCR, Extraction, Validation and Benchmark"
)

app.include_router(router)
