
# Invoice Research

## Sample Image

![invoice_sample](../![alt text](image-2.png))

# purpose
Invoices are used for billing customers and recording business transactions.

# field
Fields
Field	Description
Invoice Number	Unique invoice ID
Invoice Date	Billing date
Vendor Name	Seller
Customer Name	Buyer
GST Number	Tax ID
Items	Purchased items
Quantity	Number of units
Price	Item price
Tax	GST amount
Total Amount	Final payable amount

#JSON 
{
  "document_type": "Invoice",
  "fields": {
    "invoice_number": "",
    "invoice_date": "",
    "vendor_name": "",
    "customer_name": "",
    "gst_number": "",
    "items": [],
    "tax": "",
    "total_amount": ""
  }
}

# Validation
GST Number format
Date
Currency
Amount
# OCR Challenges
Tables
Multiple pages
Small fonts
Logos
Stamps