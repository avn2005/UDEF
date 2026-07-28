from app.validation.email_validator import validate_email
from app.validation.phone_validator import validate_phone
from app.validation.pan_validator import validate_pan
from app.validation.aadhaar_validator import validate_aadhaar
from app.validation.gst_validator import validate_gst
from app.validation.date_validator import validate_date


def validate_data(data):

	errors = {}

	if "email" in data:
		if not validate_email(data["email"]):
			errors["email"] = "Invalid Email"

	if "phone" in data:
		if not validate_phone(data["phone"]):
			errors["phone"] = "Invalid Phone Number"

	if "pan" in data:
		if not validate_pan(data["pan"]):
			errors["pan"] = "Invalid PAN"

	if "aadhaar" in data:
		if not validate_aadhaar(data["aadhaar"]):
			errors["aadhaar"] = "Invalid Aadhaar"

	if "gst" in data:
		if not validate_gst(data["gst"]):
			errors["gst"] = "Invalid GST"

	if "date" in data:
		if not validate_date(data["date"]):
			errors["date"] = "Invalid Date"

	return errors

from app.validation.valid import validate_data

sample = {
    "email": "abc@gmail.com",
    "phone": "9876543210",
    "pan": "ABCDE1234F",
    "aadhaar": "123456789012",
    "gst": "22AAAAA0000A1Z5",
    "date": "10/08/2026"
}

print(validate_data(sample))
sample = {
    "email": "abcgmail.com",
    "phone": "12345",
    "pan": "ABCDE12",
    "aadhaar": "123",
    "gst": "GST123",
    "date": "35/13/2025"
}

print(validate_data(sample))