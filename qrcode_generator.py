"""
    QrCode Generator Using Python
"""

# Importing Modules
import qrcode

# Your desired URL
input_URL = "https://www.google.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

# Inserting the URL
qr.add_data(input_URL)
qr.make(fit=True)

# Adapting the image
img = qr.make_image(fill_color="red", back_color="white")

img.save("url_qrcode.png")

print(qr.data_list)
