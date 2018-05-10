# Selenium
Selenium 是一個可以自動執行網頁操作或是拿來爬蟲的工具，因為透過開啟瀏覽器模擬使用者操作，可以執行一般爬蟲無法達到的功能 ~~自動登入自動搶票自動灌水之類的~~

範例中使用的完整程式碼請參考 example.py  
對英文有點自信的人，可以到[這個頁面](http://selenium-python.readthedocs.io)看看更完整的使用方法  

## 安裝
按照慣例，我們要透過 `pip` 安裝套件  
`pip install selenium`  

然而，為了使 Selenium 可以操作瀏覽器，我們還需要根據作業系統下載相對應的 Driver 放入適當位置：
- [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) ~~IE 表示哭哭~~
- [Firefox](https://github.com/mozilla/geckodriver/releases) (可能會需要額外步驟)
- [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) (macOS 有內建，可以不用安裝)

為了方便，下面範例皆使用 Chrome 作示範

## 基本用法
### 開啟瀏覽器
首先，新開一個資料夾，把 Chrome 的 Driver 丟進去，新增一個 Python 檔案後打入：
``` python
# coding=utf-8
from os.path import dirname

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 設定開啟的瀏覽器類型
driver = webdriver.Chrome(
    executable_path=dirname(__file__) + '/chromedriver')

# 開啟 Google 首頁
driver.get('https://www.google.com.tw/')
```

執行後，會發現桌面上開啟了一個 Chrome 的視窗，並顯示 Google 的首頁

### 選取網頁元素
在開啟網頁後，我們可以透過 Selenium 提供的方法來找到網頁上的元素 (若想要取得多個元素，可將 element 置換為 elements)：
- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

以 Google 首頁為例，開啟開發者工具後，可以找到搜尋框的 HTML 原始碼為：
``` html
<input class="gsfi" ...>
```

這時我們可以透過加入下列程式碼，將搜尋框交給 foo 變數控制：
``` python
foo = driver.find_element_by_class_name('gsfi')
```

### 輸入文字
因為我們想要輸入文字進去，可以使用 `foo.send_keys()` 告訴 Selenium 模擬鍵盤輸入：
``` python
foo.send_keys('Cat is liquid')
foo.send_keys(Keys.ENTER)
```
這會在搜尋框內輸入 `Cat is liquid` 並按下 Enter，然後你就可以找到貓卡在一堆容器裡的圖片了 OωO


## 關於爬蟲
如同一開始提到的，Selenium 可以用於爬蟲。  
透過 Requests 抓下來的內容為靜態資料，網頁在載入後透過 Javascript 追加或變更的東西會無法取得。
相對的，Selenium 是直接開啟一個瀏覽器，所有網頁流程皆與一般使用時無異，能透過程式碼即時取得元素內的資料。