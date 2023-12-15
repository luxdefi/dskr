#!/usr/bin/env python3
import qrcode
from PIL import Image, ImageDraw
import sys

def create_qr_code_with_square(data, square_image_path, output_path, qr_size=500):
        # Generate the QR code
    qr = qrcode.make(data)

    # Load the square image
    square_img = Image.open(square_image_path)

    # Calculate the new size of the square image based on the desired size
    new_size = (qr_size // 5, qr_size // 5)
    square_img = square_img.resize(new_size, Image.LANCZOS)

    # Create a new image with the same size as the QR code
    result_img = Image.new("RGB", (qr_size, qr_size), "white")

    # Paste the QR code on the new image
    result_img.paste(qr, (0, 0))

    # Calculate the position to paste the square image at the center of the QR code
    position = (
        (qr_size - new_size[0]) // 2 - 20,
        (qr_size - new_size[1]) // 2 - 20
    )

    # Paste the scaled square image in the middle of the QR code
    result_img.paste(square_img, position)

    # Save the final image
    result_img.save(output_path)

if __name__ == "__main__":
    # argument with the data you want the QR code to contain
    data = sys.argv[1]

    # Replace 'square.png' with the path to your square PNG image
    lux_image_path = "lux.png"

    # Replace 'output.png' with the desired output path
    output_path = sys.argv[2] + '.png'

    create_qr_code_with_square(data, lux_image_path, output_path)
