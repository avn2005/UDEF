# Driving license

## Sample Image

![Drive_lic](../![alt text](image-5.png))

# Purpose

Official document authorizing a person to drive.


# Fields
Field	Description
License Number	DL Number
Name	Holder
DOB	Birth date
Address	Residence
Vehicle Class	LMV, MCWG, etc.
Issue Date	Date issued
Expiry Date	Expiry
Blood Group	Blood group


# Mandatory
Mandatory	Optional
License Number	Blood Group
Name	QR Code
DOB	
Vehicle Class	
# JSON
{
  "document_type": "Driving License",
  "fields": {
    "license_number": "",
    "name": "",
    "dob": "",
    "address": "",
    "vehicle_class": "",
    "issue_date": "",
    "expiry_date": "",
    "blood_group": ""
  }
}

# Validation
License Number format
Date format
Blood Group (if present)

# OCR Challenges
Holograms
Reflection on laminated cards
Small text
State-specific layouts