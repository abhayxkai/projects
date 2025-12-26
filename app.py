import streamlit as st
import qrcode
from PIL import Image

st.title("QR Code Generator")

data = st.text_input("Enter text or URL:")
if st.button("Generate QR"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=1
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="purple", back_color="black")
    st.image(img)