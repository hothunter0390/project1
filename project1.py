import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
bs = BeautifulSoup(res.text, 'html.parser')
