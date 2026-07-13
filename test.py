import cv2
from preprocessing.deskew import deskew_image

# Load image
img = cv2.imread("sample_img/invoice.jpeg")

# Check if image loaded
if img is None:
    print("Image not found!")
    exit()

# Deskew image
result = deskew_image(img)

# Save output
cv2.imwrite("output/deskewed.jpg", result)

print("Deskew completed successfully!")
