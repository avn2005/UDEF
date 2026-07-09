# Passport 

## Sample Image

![passport](../![alt text](image-6.png))

# Purpose

International travel document.

# Fields
Field	Description
Passport Number	Passport ID
Name	Holder name
Nationality	Country
DOB	Date of Birth
Gender	Gender
Expiry Date	Expiration
Issue Date	Issued on
Place of Birth	Birth place
MRZ	Machine Readable Zone

# Mandatory
Mandatory	Optional
Passport Number	Place of Birth
Name	
Nationality	
Expiry Date

# JSON
{
  "document_type": "Passport",
  "fields": {
    "passport_number": "",
    "name": "",
    "nationality": "",
    "dob": "",
    "gender": "",
    "issue_date": "",
    "expiry_date": "",
    "mrz": ""
  }
}

# Validation
Passport Number
Date
MRZ

# OCR Challenges
MRZ reading
Small text
Reflection