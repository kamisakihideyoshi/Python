# QR Code 產生器 & Imgur 上傳器
## qrcode
官方頁面：https://github.com/lincolnloop/python-qrcode
> 使用 qrcode 之前，記得安裝 `pillow`，qrcode 生成圖片時會使用 pillow 部分的功能

```
pip install qrcode
pip install pillow
```

### qrcode_stage01.py
產生 QR Code 並保存，簡單明瞭

### qrcode_stage02.py
將 QR Code 存為 SVG 格式，並加入細部的設定

### qrcode_stage03.py
將生成 QR Code 的流程包裝成方法

### qrcode_stage04.py
加入迴圈可重複生成圖片，同時防止檔名重複

### qrcode_stage05.py
同 stage04，但使用另一種命名規則

---
## imgurpython
官方頁面：https://github.com/Imgur/imgurpython
> 安裝 imgurpython 時，會自動安裝所需的相依套件

> 在開始前，記得到 Imgur 官網申請 API，或直接點[這裏](https://api.imgur.com/oauth2/addclient)進行申請
```
pip install imgurpython
```

### imgur_stage01.py
最簡單的上傳圖片方法

### imgur_stage02.py
為你的圖片加點描述

### imgur_stage03.py
結合 QR Code 產生器，將 QR Code 直接傳到 Imgur 上