# Universal Document Extraction Framework (UDEF)

# Universal Document Extraction Framework (UDEF)

## Framework Architecture

**Version:** 1.0  
**Project Type:** Internal Research & Development  
**Department:** Artificial Intelligence

---

# 1. Objective

The Universal Document Extraction Framework (UDEF) is designed to extract structured information from different document types using OCR and Large Language Models (LLMs). The framework follows a modular architecture to ensure scalability, reusability, and easy maintenance.

---

# 2. Project Folder Structure

```text
UDEF/
│
├── app/
│   ├── api/
│   ├── preprocessing/
│   ├── ocr/
│   ├── extractor/
│   ├── validation/
│   ├── formatter/
│   ├── benchmark/
│   └── templates/
│
├── datasets/
├── docs/
├── outputs/
├── sample_documents/
├── tests/
├── requirements.txt
├── README.md
└── main.py
```

---

# 3. Folder Description

| Folder | Description |
|---------|-------------|
| app/api | REST API endpoints using FastAPI |
| app/preprocessing | Image preprocessing using OpenCV |
| app/ocr | OCR engines (Tesseract, EasyOCR, PaddleOCR) |
| app/extractor | AI-based field extraction using Gemini |
| app/validation | Validation of extracted fields |
| app/formatter | Converts extracted data into JSON |
| app/benchmark | OCR benchmarking and evaluation |
| app/templates | Document templates and prompts |
| datasets | Sample datasets for testing |
| docs | Project documentation |
| outputs | Extracted JSON outputs |
| tests | Unit and integration tests |

---

# 4. Module Boundaries

## Input Module

### Responsibility

- Accept image or PDF files
- Validate file format

**Input**

- JPG
- PNG
- PDF

**Output**

Validated document

---

## Image Preprocessing Module

### Responsibility

- Convert image to grayscale
- Noise removal
- Thresholding
- Deskewing
- Resize image

**Input**

Document image

**Output**

Enhanced image

---

## OCR Module

### Responsibility

Extract text using multiple OCR engines.

Supported OCR:

- Tesseract OCR
- EasyOCR
- PaddleOCR

**Input**

Preprocessed image

**Output**

Raw extracted text

---

## AI Extraction Module

### Responsibility

Uses Gemini LLM to identify important fields.

Examples:

- Resume
- Invoice
- PAN Card
- Aadhaar Card

**Input**

OCR Text

**Output**

Structured document fields

---

## Validation Module

### Responsibility

Validate extracted values.

Examples:

- Email
- Phone Number
- PAN Number
- Aadhaar Number
- Date Format

**Output**

Validated information

---

## JSON Formatter

### Responsibility

Convert extracted information into a standard JSON structure.

---

## REST API Module

### Responsibility

Provide APIs for external applications.

---

# 5. Processing Flow

```text
Upload Document
        │
        ▼
Input Validation
        │
        ▼
Image Preprocessing
        │
        ▼
OCR Engine
        │
        ▼
Extracted Text
        │
        ▼
Gemini LLM
        │
        ▼
Field Extraction
        │
        ▼
Validation
        │
        ▼
JSON Formatter
        │
        ▼
REST API Response
```

---

# 6. Data Flow

```text
User
   │
   ▼
Upload Document
   │
   ▼
Image Preprocessing
   │
   ▼
OCR Engine
   │
   ▼
Extracted Text
   │
   ▼
AI Extraction
   │
   ▼
Validation
   │
   ▼
JSON Output
```

---

# 7. REST API Design

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /extract | Extract document information |
| POST | /ocr | OCR only |
| GET | /health | Health check |
| GET | /supported-documents | List supported document types |

---

# 8. Sample API Request

```json
{
  "file": "resume.pdf"
}
```

---

# 9. Sample API Response

```json
{
  "document_type": "Resume",
  "fields": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210"
  }
}
```

---

# 10. System Architecture

```text
                User
                  │
                  ▼
          Upload Document
                  │
                  ▼
       Input Validation Layer
                  │
                  ▼
      Image Preprocessing Module
                  │
                  ▼
          OCR Engine Layer
    ┌────────┬─────────┬─────────┐
    │        │         │
Tesseract EasyOCR PaddleOCR
                  │
                  ▼
          OCR Extracted Text
                  │
                  ▼
      AI Extraction Module
          (Gemini API)
                  │
                  ▼
         Validation Module
                  │
                  ▼
          JSON Formatter
                  │
                  ▼
          FastAPI REST API
                  │
                  ▼
          Client Application
```

---

# 11. Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| API Framework | FastAPI |
| OCR Engines | PaddleOCR, EasyOCR, Tesseract |
| Image Processing | OpenCV |
| AI Model | Gemini API |
| Validation | Pydantic |
| Version Control | Git |

---

# 12. Advantages

- Modular architecture
- Easy to maintain
- Reusable OCR framework
- Supports multiple OCR engines
- Supports multiple document types
- Easy integration with AI models
- Standardized JSON output
- Easily extensible

---

# 13. Conclusion

The UDEF framework follows a modular architecture that separates preprocessing, OCR, AI extraction, validation, and API services. This design improves maintainability, scalability, and allows new document types and OCR engines to be integrated with minimal changes.