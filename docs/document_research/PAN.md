# PAN Card Research
## Purpose

The Permanent Account Number (PAN) Card is an identity document issued by the Income Tax Department of India.

It is mainly used for:

- Income tax filing
- Financial transactions
- Opening bank accounts
- Identity verification
- Applying for loans
## Sample Image

![PAN Sample](../![alt text](image.png))

## Fields to Extract

| Field | Description |
|-------|-------------|
| Name | Card holder's full name |
| Father's Name | Father's full name |
| Date of Birth | Card holder's date of birth |
| PAN Number | Permanent Account Number |
| Signature | Card holder's signature |
| QR Code | QR Code if available |

## Mandatory vs Optional Fields

| Mandatory | Optional |
|------------|----------|
| PAN Number | Signature |
| Name | QR Code |
| Father's Name | |
| Date of Birth | |

JSON SCHEMA 
{
  "document_type": "PAN",
  "fields": {
    "name": "Rahul Sharma",
    "father_name": "Rajesh Sharma",
    "dob": "15/06/1995",
    "pan_number": "ABCDE1234F",
    "signature": "Present"
  }
}

## JSON Schema

```json
{
  "document_type": "PAN",
  "fields": {
    "name": "",
    "father_name": "",
    "dob": "",
    "pan_number": "",
    "signature": ""
  }
}
```

## Validation Rules

| Field | Validation |
|-------|------------|
| PAN Number | Five uppercase letters, four digits, one uppercase letter (e.g., ABCDE1234F) |
| Date of Birth | DD/MM/YYYY |
| Name | Alphabetic characters only |
| Father's Name | Alphabetic characters only |

## OCR Challenges

- Low-quality scans
- Blurry images
- Cropped document
- Glare on laminated card
- Rotated or tilted document
- Small font size
- Signature overlapping text
