import streamlit as st
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("Image to Text Converter")


def convert(photo):
    st.image(photo)
    img = Image.open(photo)
    text = pytesseract.image_to_string(img)
    # text = pytesseract.image_to_string(img, lang='hin')
    st.header("Your text is:")
    st.write(text)


choice = st.selectbox("Upload Image via",
                      ("Select",
                       "Camera",
                       "File browser"))

if choice == "Camera":
    with st.expander("Start Camera"):
        camera_image = st.camera_input("Camera")
    if camera_image:
        convert(camera_image)
elif choice == "File browser":
    uploaded_image = st.file_uploader('Upload image', type=['png', 'jpg', 'jpeg'])
    if uploaded_image:
        convert(uploaded_image)
