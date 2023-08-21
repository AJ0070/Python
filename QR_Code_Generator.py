import qrcode

# Get user input for the text to encode
data = input("Enter the text: ")

# Get user input for the file name and location
file_name = input("Enter the file name (e.g., example_qr_code.png): ")
file_location = input("Enter the file location (e.g., /path/to/save/location/): ")

# Generate a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create a QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image with the user-specified file name and location
save_path = file_location + file_name
img.save(save_path)

print(f"QR code saved to {save_path}")
    