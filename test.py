import pytesseract
from PIL import Image

# Tell Python where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("Opening image...")

img = Image.open("sample.png")

print("Extracting text...")

text = pytesseract.image_to_string(img)

print("Detected Text:")
print("----------------")
print(text)

harmful_ingredients = ["Sugar", "Salt", "Paraben", "Sodium Benzoate"]

found = []

for ingredient in harmful_ingredients:
    if ingredient.lower() in text.lower():
        found.append(ingredient)

print("\nHarmful Ingredients Found:")
print("---------------------------")

if found:
    for item in found:
        print(item)
else:
    print("None detected")
