import qrcode

data = input("Enter the text or link to generate QR code: ")

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR Code generated successfully! Saved as qrcode.png")
