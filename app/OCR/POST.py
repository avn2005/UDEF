@router.post("/extract")
async def extract_document(file: UploadFile = File(...)):

    result = {
        "name": "John Doe",
        "email": "john@gmail.com"
    }

    return {
        "status": "success",
        "data": result
    }