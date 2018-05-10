# coding=utf-8
import qrcode

# 引入 svg 的描述
import qrcode.image.svg as qrsvg

# 將物件 QRCode 存入變數 qr:
# version -- 影響 QR Code 的格數和信息量，範圍: 1~40，或設為 None 自動調整
# 詳細內容可參考: http://www.qrcode.com/en/about/version.html
# error_correction -- 容錯率，可選 ERROR_CORRECT_L (7%), M (15%), Q (25%), H (30%)
# box_size -- QR Code 每格的大小
# border -- QR Code 四個邊預留的格數
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=50,
    border=4,
)

# 若上方的 version 設為 None 可加上，不過其實沒什麼用
# qr.make(fit=True)

# 加入 QR Code 裡面想包的文字、連結:
qr.add_data('This is a test')

# 生成圖片:
# image_factory -- SVG 的輸出類型，設為 None 輸出一般圖片
# SvgFragmentImage 可單獨編輯每個黑色格子, SvgPathImage 將所有格子轉為單一路徑
# fill_color, back_color -- 只作用在一般圖片，分別為背景顏色及格子的顏色，格式為字串
# 範例: qr.make_image(fill_color='white', back_color='black')
image = qr.make_image(image_factory=qrsvg.SvgPathImage)

image.save('qrcode.png')
