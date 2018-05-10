import requests
from bs4 import BeautifulSoup

result = requests.get('https://google.com.tw')
print(result.text)

soup = BeautifulSoup(result.text)
