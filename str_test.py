import re

str='電話番号：0-3574-6591-7  FAX番号： 0-3574-6590 伊藤： ito@thaimikami.com'

pattern = re.compile(r' |\xa0')

result = pattern.split(str)

print(result)