import re

def validate_aadhaar(aadhaar):
    pattern = r'^\d{12}$'
    return bool(re.match(pattern, aadhaar))
