from bs4 import *
with open('sait.html','r',encoding='utf-8') as r:
    soup = BeautifulSoup(r,'lxml')
body = soup.body

# print(body.get_text())
# print(body.string)
print(soup.findAll('center'))
