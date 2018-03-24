import qrcode

import tempfile

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

client_id = '你的 id'
client_secret = '你的 secret'

client = ImgurClient(client_id, client_secret)


def get_qrcode_link(text):
    '''
    生成 QR Code 並回傳在 Imgur 上的連結

    Argument:
    text -- 存入 QR Code 的文字、網址
    '''
    image = qrcode.make(text)

    # 創建一個暫存並讓 QR Code 存進去
    temp = tempfile.NamedTemporaryFile()
    image.save(temp)

    config = {
        'name': 'Useless QR Code',
        'title': 'Useless QR Code',
        'description': 'Just an useless QR Code OωO'
    }

    try:
        print('圖片上傳中...')
        upload_result = client.upload_from_path(
            temp.name, config=config, anon=True)

        temp.close()
        return upload_result['link']

    except ImgurClientError as e:
        print('好像出了點問題 (´･ω･`)')
        print('狀態', e.status_code, '，錯誤訊息:', e.error_message)

        temp.close()
        return None


while True:
    content = input('請輸入想要儲存在 QR Code 的內容：')
    link = get_qrcode_link(content)

    # 當上傳失敗，get_qrcode_link() 回傳 None 時的處理方法:
    if link is None:
        print('上傳失敗，請重試一次')

    print('上傳成功 OωO\n連結:', link)
