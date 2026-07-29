datasets/
├── resume/
├── invoice/
├── business_card/
├── aadhaar/
└── pan/

Input Document
      ↓
Image Preprocessing
      ↓
OCR Engine
      ↓
LLM Extraction
      ↓
JSON Validation
      ↓
REST API
      ↓
Structured JSON Output


# demonstration
Start the application.
Open Swagger UI (if using FastAPI).
Upload a sample document.
Run OCR.
Extract structured data.
Display the JSON output.
Show validation results.
Test with another document type.
# table
Metric	Result
Documents Tested	100
OCR Accuracy	95%
Extraction Accuracy	94%
Average Processing Time	1.8 sec
Memory Usage	180 MB

# lesson learned 

Designing modular software architecture.
Integrating OCR with LLMs.
Creating REST APIs using FastAPI.
Writing JSON schemas and validations.
Benchmarking OCR performance.
Debugging and testing AI applications.
Using Git and GitHub for version control.

