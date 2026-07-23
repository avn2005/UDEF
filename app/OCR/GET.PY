@router.get("/supported-documents")
async def supported_documents():

    return {
        "documents": [
            "Resume",
            "Invoice",
            "Business Card",
            "PAN",
            "Aadhaar",
            "Passport"
        ]
    }