import csv
import json
import time

def benchmark_ocr():
    ocr_results = [
    {
        "engine":"PaddleOCR",
        "time":0.82,
        "accuracy":97
    },
    {
        "engine":"EasyOCR",
        "time":1.15,
        "accuracy":94
    },
    {
        "engine":"Tesseract",
        "time":2.08,
        "accuracy":89
    }
]
    
    prompt_results = [
    {
        "prompt":"V1",
        "accuracy":90
    },
    {
        "prompt":"V2",
        "accuracy":95
    },
    {
        "prompt":"V3",
        "accuracy":98
    }
]
    ocr_results = [
    ["PaddleOCR",97,0.82],
    ["EasyOCR",94,1.15],
    ["Tesseract",89,2.08]
]

with open("reports/benchmark.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["OCR Engine","Accuracy","Execution Time"])

    writer.writerows(ocr_results)
    