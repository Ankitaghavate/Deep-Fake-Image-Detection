import streamlit as st
from detect import detect_deepfake
from utils.preprocessing import preprocess_image
import cv2

st.title("Deepfake Image Detector")

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    # Save the uploaded file
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Detect deepfake
    result = detect_deepfake("temp_image.jpg")
    st.write(f"**Result:** {result}")
    
    # Display the image
    image = cv2.imread("temp_image.jpg")
    st.image(image, caption='Uploaded Image', use_column_width=True)