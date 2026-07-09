# Aadhar Card 

## Sample Image

![aadhar_card](../![alt text](image-3.png))

# Fields
Field	Description
Aadhaar Number	12-digit number
Name	Holder name
DOB	Date of Birth
Gender	Male/Female
Address	Residential address
QR Code	QR
# Mandatory
Mandatory	Optional
Aadhaar Number	QR Code
Name	Address
DOB	
# JSON
{
  "document_type": "Aadhaar",
  "fields": {
    "aadhaar_number": "",
    "name": "",
    "dob": "",
    "gender": "",
    "address": ""
  }
}

# Validation
Aadhaar → 12 digits
DOB
Gender
OCR Challenges
Hindi + English text
QR Code
Glare
Cropped image