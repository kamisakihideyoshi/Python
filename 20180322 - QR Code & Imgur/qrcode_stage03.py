# coding=utf-8
import qrcode
import qrcode.image.svg as qrsvg

# 將生成 QR Code 的流程包裝成方法


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

    # 判斷是否存成 SVG 格式:
    if svg == True:
        factory = qrsvg.SvgPathFillImage
        image = qr.make_image(image_factory=factory)
        image.save('qrcode.svg')
        return

    image = qr.make_image()
    image.save('qrcode.png')


qrcode_gen('This is a test', svg=True)
