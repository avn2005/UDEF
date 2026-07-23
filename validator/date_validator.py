from datetime import datetime

def validate_date(date):
	try:
		datetime.strptime(date, "%d/%m/%Y")
		return True
	except Exception:
		return False

