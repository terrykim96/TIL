import requests
from bs4 import BeautifulSoup

# 코스피

# 코스피 받아올 페이지
response = requests.get('https://finance.naver.com/sise/').text

# Beautifulsoup과 selector 이용하여 원하는 것 가져오기
bs = BeautifulSoup(response, 'html.parser').select_one('#KOSPI_now')
kospi = bs.text

print(kospi)

# 환율

# 환율 받아올 페이지
response1 = requests.get('https://finance.naver.com/marketindex/').text

# Beautifulsoup과 selector 이용하여 원하는 것 가져오기
bs1 = BeautifulSoup(response1, 'html.parser').select_one('#exchangeList > li.on > a.head.usd > div > span.value')
exchange = bs1.text
print(exchange)

