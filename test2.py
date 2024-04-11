import requests
from bs4 import BeautifulSoup

url='https://www.fact-link.com/search_cate.php?lang=jp&ctrid=006'

url_next = 'https://www.fact-link.com/search_cate.php?offset=30'

url_next_2 = 'https://www.fact-link.com/search_cate.php?offset=120'

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

print(rs.text)

rs2 = requests.get(url=url_next, headers=headers)
#print(rs2.text)

rs3 = requests.get(url=url_next_2, headers=headers)
#print(rs3.text)

soup = BeautifulSoup(rs3.text, features='html.parser')
divs_cp = soup.find_all('div', class_='cp')

next_btn = soup.find('a', text= '次へ')

for div_cp in divs_cp:
    div_cp_sp = BeautifulSoup(str(div_cp), features='html.parser')

    p_corp = div_cp_sp.find('p', class_='corp')
    company_name = p_corp.text

    a_jp = div_cp_sp.find('a', class_='jp')
    if a_jp != None:
        company_link = a_jp['href']
    else:
        a_en = div_cp_sp.find('a', class_='en')
        if a_en != None:
            company_link = a_en['href']
        else:
            a_th = div_cp_sp.find('a', class_='th')
            if a_th != None:
                company_link = a_th['href']
            else:
                company_link = None

    if company_link:
        company_link = str(company_link).replace('mem_content', 'mem_profile')
    print(company_name)
    print(company_link)

if next_btn:
    print(next_btn, '\n',next_btn['href'])