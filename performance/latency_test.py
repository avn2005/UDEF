from fastapi import APIRouter, UploadFile, File
from typing import Any


def load_model() -> Any:
    # Replace this with your actual model loading logic
    class DummyModel:
        def predict(self, file: UploadFile):
            return {"filename": file.filename}

    return DummyModel()


model = load_model()  # Load once
router = APIRouter()


@router.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    result = model.predict(file)
    return {"result": result}

image = cv2.imread(path)
image = cv2.resize(image, (1000, 1000))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)