from bs4 import BeautifulSoup as BS 
import requests
from datetime import date, datetime

data = datetime.now()
datenow = str(data.day) + "-" + str(data.month) + "-" + str(data.year)

allvac = []

url = 'https://jobs.dou.ua/vacancies/?city=Киев&search=.net'
url2 = 'https://jobs.dou.ua/vacancies/?city=Киев&search=.net+core'
url3 = 'https://jobs.dou.ua/vacancies/?city=Киев&search=.net+angular'
url4 = 'https://jobs.dou.ua/vacancies/?city=Киев&search=.net+full-stack'
url5 = 'https://jobs.dou.ua/vacancies/?city=Киев&search=.net+fullstack'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
FILENAME = datenow + ".csv"

def csvWrite(fullword):
    with open(FILENAME, "a") as f:
        f.write(fullword)



r = requests.get(url, headers=headers)
html = BS(r.content, 'html.parser')

vac = html.find(class_="l-vacancy")
#comp = html.find(class_="company")
city = html.find(class_="cities")

print(".net \n\n")
for vac in html.find_all(class_='l-vacancy'):
    title = vac.div.div.a.text
    if title in allvac:
        continue
    else:
        allvac.append(title)
    company = vac.div.div.strong.a.text
    for city in html.find_all(class_="cities"):
        citys = city.text
    fullword = title + "," + company + "," + citys +"\n"
    csvWrite(fullword)

r = requests.get(url2, headers=headers)
html = BS(r.content, 'html.parser')
print(".net core\n\n")
for vac in html.find_all(class_='l-vacancy'):
    title = vac.div.div.a.text
    if title in allvac:
        continue
    else:
        allvac.append(title)
    company = vac.div.div.strong.a.text
    for city in html.find_all(class_="cities"):
        citys = city.text
    fullword = title + "," + company + "," + citys +"\n"
    csvWrite(fullword)

r = requests.get(url3, headers=headers)
html = BS(r.content, 'html.parser')
print(".net angular\n\n")
for vac in html.find_all(class_='l-vacancy'):
    title = vac.div.div.a.text
    if title in allvac:
        continue
    else:
        allvac.append(title)
    company = vac.div.div.strong.a.text
    for city in html.find_all(class_="cities"):
        citys = city.text
    fullword = title + "," + company + "," + citys +"\n"
    csvWrite(fullword)

r = requests.get(url4, headers=headers)
html = BS(r.content, 'html.parser')
print(".net full-stack\n\n")
for vac in html.find_all(class_='l-vacancy'):
    title = vac.div.div.a.text
    if title in allvac:
        continue
    else:
        allvac.append(title)
    company = vac.div.div.strong.a.text
    for city in html.find_all(class_="cities"):
        citys = city.text
    fullword = title + "," + company + "," + citys +"\n"
    csvWrite(fullword)

r = requests.get(url4, headers=headers)
html = BS(r.content, 'html.parser')
print(".net fullstack\n\n")
for vac in html.find_all(class_='l-vacancy'):
    title = vac.div.div.a.text
    if title in allvac:
        continue
    else:
        allvac.append(title)
    company = vac.div.div.strong.a.text
    for city in html.find_all(class_="cities"):
        citys = city.text
    
    


