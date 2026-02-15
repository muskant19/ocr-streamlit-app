import streamlit as st
import pytesseract
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Ingredient Scanner", layout="centered")

st.title("🥗 Smart Ingredient Scanner")

uploaded_file = st.file_uploader("Upload Food Label Image", type=["jpg","png","jpeg"])

danger_ingredients = ["milk", "soy", "wheat", "peanut", "almond", "egg", "gluten"]

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)

    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)
    text_lower = text.lower()

    st.subheader("📄 Extracted Ingredients:")
    st.write(text)

    st.subheader("⚠ Allergy Check:")

    found = False
    for item in danger_ingredients:
        if item in text_lower:
            st.error(f"⚠ Contains: {item.upper()}")
            found = True

    if not found:
        st.success("✅ No common allergens detected!")
