# Requests & Beautiful Soup 4
## Requests
Requests 是一個處理網路請求的套件，可以用簡短的程式碼上傳、下載的動作  
對英文有點自信的人，可以到[這個頁面](http://docs.python-requests.org/en/master/)看看更完整的使用方法  
### 基本用法
``` python
# coding=utf-8
import requests

result = requests.get('https://www.google.com.tw/')
print(result.text)

```

## Beautiful Soup 4
Beautiful Soup 是一個解析 (parse) HTML 的套件，
### 基本用法
``` python
# coding=utf-8
import requests
from bs4 import Beautifulsoup

result = requests.get('https://www.google.com.tw/')
soup = Beautifulsoup(result.text)

```
`print(soup.prettify())`
`soup.body`