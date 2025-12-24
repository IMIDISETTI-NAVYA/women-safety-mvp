import qrcode

drivers = ["AUT0101", "AUT9999"]  # Verified & Unverified

for driver_id in drivers:
    data = f"http://localhost:5000/driver/{driver_id}"
    qr = qrcode.make(data)
    file_name = f"{driver_id}_QR.png"
    qr.save(file_name)
    print(f"{file_name} generated")
