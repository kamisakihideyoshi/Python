from imgurpython import ImgurClient

# 引入 imgurpython 的錯誤處理方式
from imgurpython.helpers.error import ImgurClientError

client_id = '你的 id'
client_secret = '你的 secret'

client = ImgurClient(client_id, client_secret)

# 設定在 Imgur 中顯示的資訊
config = {
    'name': '圖片的名稱',
    'title': '圖片的標題',
    'description': '圖片的描述'
}


try:
    print('圖片上傳中...')

    # config -- 在 Imgur 中顯示的資訊
    # anon -- 是否匿名，不過看起來沒什麼差別
    upload_result = client.upload_from_path(
        '圖片的名稱', config=config, anon=True)
    print('上傳成功 OωO\n連結:', upload_result['link'])

# 錯誤處理:
except ImgurClientError as e:
    print('好像出了點問題 (´･ω･`)')
    print('狀態', e.status_code, '，錯誤訊息:', e.error_message)
