
from typing import Union

def extract_text(image: Union[str, bytes, 'PIL.Image.Image', 'numpy.ndarray'], engine: str = "tesseract") -> str:
	"""Extract text from an image using the specified OCR engine.

	image: file path, bytes, PIL Image or numpy array.
	engine: one of "tesseract", "easyocr", "paddle".
	"""
	engine = engine.lower()

	if engine == "tesseract":
		try:
			from PIL import Image
			import pytesseract
		except Exception as e:
			raise RuntimeError("tesseract dependencies not available: " + str(e))

		if isinstance(image, str):
			img = Image.open(image)
		elif hasattr(image, 'read'):
			img = Image.open(image)
		else:
			img = image

		return pytesseract.image_to_string(img)

	if engine == "easyocr":
		try:
			import easyocr
			import numpy as np
			from PIL import Image
		except Exception as e:
			raise RuntimeError("easyocr dependencies not available: " + str(e))

		if isinstance(image, str):
			img = Image.open(image)
			img = np.array(img.convert('RGB'))
		elif hasattr(image, 'read'):
			img = Image.open(image)
			img = np.array(img.convert('RGB'))
		else:
			img = image

		reader = easyocr.Reader(['en'], gpu=False)
		results = reader.readtext(img)
		return "\n".join([r[1] for r in results])

	if engine == "paddle":
		try:
			from paddleocr import PaddleOCR
			from PIL import Image
			import numpy as np
		except Exception as e:
			raise RuntimeError("paddleocr dependencies not available: " + str(e))

		if isinstance(image, str):
			img_path = image
		elif hasattr(image, 'filename'):
			img_path = image.filename
		else:
			# write numpy or PIL to temporary file
			import tempfile
			if hasattr(image, 'save'):
				tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
				image.save(tmp.name)
				img_path = tmp.name
			else:
				# assume numpy array
				tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
				Image.fromarray(image).save(tmp.name)
				img_path = tmp.name

		ocr = PaddleOCR(use_angle_cls=True, lang='en')
		res = ocr.ocr(img_path, cls=True)
		lines = []
		for page in res:
			for box, txt, conf in page:
				lines.append(txt)
		return "\n".join(lines)

	raise ValueError(f"Unsupported engine: {engine}")
