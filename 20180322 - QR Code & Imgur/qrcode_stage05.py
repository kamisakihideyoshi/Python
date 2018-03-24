# coding=utf-8
import qrcode
import qrcode.image.svg as qrsvg

import datetime


def qrcode_gen(text, svg=False):
    """生成 QR Code 的方法

    Arguments:
    text -- 存入 QR Code 的文字、網址
    svg -- 是否存為 svg 格式 (預設為 None)
    """

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=50,
        border=4,
    )

    qr.add_data(text)

    # 透過 datetime 取得目前時間:
    current_date = datetime.datetime.now()

    # 將時間以指定格式輸出:
    # %y, %Y -- 年
    # %m, %d -- 月、日
    # %H, %M, %S -- 時、分、秒
    current_date_string = current_date.strftime(r'%Y年%m月%d日%H時%M分%S秒')

    if svg == True:
        factory = qrsvg.SvgPathFillImage
        image = qr.make_image(image_factory=factory)
        image.save(current_date_string + '.svg')
        return

    image = qr.make_image()
    image.save(current_date_string + '.png')


while True:
    content = input('請輸入想要儲存在 QR Code 的內容：')
    svg = input('是否存為 SVG 格式 (Y/N)：')

    if svg.lower() == 'y':
        qrcode_gen(content, svg=True)
        continue

    qrcode_gen(content)
