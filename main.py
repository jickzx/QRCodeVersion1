import qrcode

while True:

    ask = input("Do you want to generate another QR code? (y/n): ").strip().lower()
    if ask == "y":
        url = input("enter the URL: ").strip()
        file_path_name = input("create file path name without png: ")

        file_path = f"E:\\Coding\\Qr Code Generator\\Qr Code Images\\{file_path_name}.png"

        qr = qrcode.QRCode()
        qr.add_data(url)

        img = qr.make_image()
        img.save(file_path)

        print(f"QR Code generated and saved at: {file_path}")

    # end qr code generator
    elif ask == "n":
        print("QR Code generation ended")
        False
        break   # exits the loop

    # != y,n
    else:
        print("Invalid input. Please enter y/n")

