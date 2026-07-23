model = load_model()   # Load once

@router.post("/ocr")
async def ocr(file: UploadFile):
    result = model.predict(file)