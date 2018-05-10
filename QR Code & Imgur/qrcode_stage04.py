# coding=utf-8
import qrcode
import qrcode.image.svg as qrsvg

# Python 內建的正規表達式套件
import re


def qrcode_gen(text, svg=False):
    """生成 QR Code 的方法

    Arguments:
    text -- 存入 QR Code 的文字、網址
    svg -- 是否存為 SVG 格式 (預設為 None)
    """

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=50,
        border=4,
    )

    qr.add_data(text)

    # print('原始內容:', text)
    # 利用 re 尋找所有非文字的內容，並以 _ 取代:
    for i in re.findall(r'\W', text):
        # print(i)
        text = text.replace(i, '_')
    # print('修改過內容:', text)

    # 判斷是否存成 SVG 格式:
    if svg == True:
        factory = qrsvg.SvgPathFillImage
        image = qr.make_image(image_factory=factory)
        image.save(text + '.svg')
        return

    image = qr.make_image()
    image.save(text + '.png')


while True:
    content = input('請輸入想要儲存在 QR Code 的內容：')
    svg = input('是否存為 SVG 格式 (Y/N)：')

    if svg.lower() == 'y':
        qrcode_gen(content, svg=True)
        continue

    qrcode_gen(content)
