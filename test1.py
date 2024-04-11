import requests
from bs4 import BeautifulSoup

url = 'https://www.fact-link.com/'

headers = {
    'authority': 'www.fact-link.com',
    'method': 'GET',
    'path': "/",
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': "ja,zh-TH;q=0.9,zh;q=0.8,th-TH;q=0.7,th;q=0.6,en-TH;q=0.5,en-US;q=0.4,en;q=0.3",
    'Cache-Control': 'max-age=0',
    'Cookie': 'lang=jp; __utmz=118580510.1711683656.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.1.827601414.1711683657; cookieControl=true; cookieControlPrefs=["preferences","analytics","marketing"]; PHPSESSID=poa9f0pcjql3tqcra407laanr2; __utma=118580510.57685764.1711683656.1712107907.1712121888.5; __utmc=118580510; _ga_T8H0BLR4NB=GS1.1.1712121769.5.1.1712121891.0.0.0; __utmt=1; __utmb=118580510.7.10.1712121888; _ga_5SYSWMEFJ3=GS1.1.1712121887.4.1.1712122795.0.0.0',
    'Referer': 'https://www.fact-link.com/',
    'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

rs = requests.get(url=url, headers=headers)
#print(rs.text)

soup = BeautifulSoup(rs.text, features='html.parser')

section = soup.find('section', class_='category')

#print(section)
#print(type(section))

menu_sp = BeautifulSoup(str(section), features='html.parser')

menu = menu_sp.find('div', class_='menu')

category_sp = BeautifulSoup(str(menu), features='html.parser')

category = category_sp.find_all('a')

for each in category:
    print(each.text)
    print(each['href'])