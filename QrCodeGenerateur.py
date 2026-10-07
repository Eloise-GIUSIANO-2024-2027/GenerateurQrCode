import qrcode

print("Quel lien voulez vous transformer en QR code ?")
link = input()
img = qrcode.make(link)
img.save('Image/qrcode.png')