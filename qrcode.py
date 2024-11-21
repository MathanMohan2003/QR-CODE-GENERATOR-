import qrcode
img = qrcode.make("https://learningcentral.tataelxsi.co.in/login/index.php")
img.save("my_tata.jpg")
print("won")