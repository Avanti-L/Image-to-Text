import streamlit as st
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

st.title("Image to Text Converter")


choice = st.selectbox("Upload Image via",
                      ["Camera",
                       "File browser"])

col1, col2 = st.columns(2)
data = None
text = None

with col1:
    if choice == "Camera":
        with st.expander("Start Camera"):
            data = st.camera_input("Camera")
    elif choice == "File browser":
        data = st.file_uploader('Upload image', type=['png', 'jpg', 'jpeg'])

with col2:
    if data:
        st.image(data)
        img = Image.open(data)
        text = pytesseract.image_to_string(img, lang='eng+hin')

st.markdown("----")

if text:
    col3, col4 = st.columns(2)

    with col3:
        st.code(text, language='text')

    with col4:
        st.text_area("Copy and paste the result here", height=400)
