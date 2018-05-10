# codeing=utf-8
# 從 imgur 的套件引入處理上傳的物件
from imgurpython import ImgurClient

# 填入自己申請的 API id 跟 secret，創建處理 imgur 上傳的物件:
# 若無申請過，請至: https://api.imgur.com/oauth2/addclient 取得 API 的 id 跟 secret
client_id = '你的 id'
client_secret = '你的 secret'

client = ImgurClient(client_id, client_secret)

# 上傳指定路徑的圖片，注意無法上傳 SVG 格式:
result = client.upload_from_path('圖片的名稱')

# 顯示圖片的網址
print(result['link'])
