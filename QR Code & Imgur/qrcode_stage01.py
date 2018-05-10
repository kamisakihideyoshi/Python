# coding=utf-8
# 引入 QR Code 套件:
import qrcode

# 透過套件生成 QR Code 的圖片，並存入變數 image:
# qrcode.make('你的 QR Code 裡面想包的文字、連結')
image = qrcode.make('This is a test')

# 將變數 image 裡面的圖片存成檔案:
# 副檔名可以隨便打，但內部格式一律為 png
# image.save('圖片儲存的名稱.png')
image.save('qrcode.png')
