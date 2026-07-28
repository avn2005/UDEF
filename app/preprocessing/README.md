# Universal Document Extraction Framework (UDEF)
## Image Preprocessing Module

### Project Overview

The Image Preprocessing Module is a reusable Python library developed as part of the Universal Document Extraction Framework (UDEF). It prepares scanned documents and images for OCR by improving image quality and correcting common issues such as skew, rotation, noise, low contrast, and inconsistent image size.

The processed images can be directly used with OCR engines like Tesseract, EasyOCR, and PaddleOCR for improved text extraction accuracy.

---

## Features

- Resize images while maintaining aspect ratio
- Deskew tilted documents
- Correct image rotation
- Remove image noise
- Enhance image contrast
- Adaptive thresholding for OCR
- Modular and reusable architecture

---

## Project Structure

```
UDEF/
│
├── preprocessing/
│   ├── __init__.py
│   ├── resize.py
│   ├── deskew.py
│   ├── rotation.py
│   ├── noise.py
│   ├── contrast.py
│   ├── threshold.py
│   └── preprocess.py
│
├── sample_img/
│   ├── invoice.jpeg
│   ├── receipt.jpg
│   ├── aadhar.jpg
│   └── passport.jpg
│
├── output/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

- Python 3.11+
- OpenCV
- NumPy
- Pillow
- SciPy
- Matplotlib

---

## Installation

Clone the repository

```bash
git clone <repository_url>
```

Move into the project directory

```bash
cd UDEF
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```
opencv-python
numpy
Pillow
scipy
matplotlib
```

---

## Module Description

### resize.py

Resizes document images while preserving aspect ratio.

### deskew.py

Detects and corrects tilted scanned documents.

### rotation.py

Corrects images rotated by 90°, 180°, or 270°.

### noise.py

Removes scanner noise using image filtering techniques.

### contrast.py

Enhances document readability using Histogram Equalization and CLAHE.

### threshold.py

Applies binary, Otsu, and adaptive thresholding methods for OCR-ready images.

### preprocess.py

Runs the complete preprocessing pipeline.

---

## Processing Pipeline

```
Input Image
      │
      ▼
Resize
      │
      ▼
Deskew
      │
      ▼
Rotation Correction
      │
      ▼
Noise Removal
      │
      ▼
Contrast Enhancement
      │
      ▼
Adaptive Thresholding
      │
      ▼
Processed Image
```

---

## Sample Input

```
sample_img/
    invoice.jpeg
    receipt.jpg
    aadhar.jpg
    passport.jpg
```

---

## Sample Output

```
output/

invoice_processed.jpg

receipt_processed.jpg

aadhar_processed.jpg

passport_processed.jpg
```

---

## How to Run

Run the preprocessing pipeline

```bash
python preprocessing/preprocess.py
```

Or run an individual module for testing.

Example

```bash
python tests/test_preprocessing.py
```

---

## Deliverables

- Image Resize Module
- Deskew Module
- Rotation Correction Module
- Noise Removal Module
- Contrast Enhancement Module
- Adaptive Thresholding Module
- Integrated Preprocessing Pipeline
- Sample Input Images
- Processed Output Images
- Documentation

---

## Future Enhancements

- Automatic document orientation detection
- PDF preprocessing support
- Batch image processing
- Multi-language OCR support
- Integration with Tesseract, EasyOCR, and PaddleOCR

---

## Author

**Avanti Hedau**

AI & ML Intern

ICT INSTA Solutions Pvt. Ltd.

B.Tech Artificial Intelligence

---

## License

This project is developed for educational and internship purposes.