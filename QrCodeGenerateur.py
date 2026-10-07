import qrcode

img = qrcode.make('https://www.youtube.com/')
img.save('Image/qrcode.png')