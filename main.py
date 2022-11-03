import lxml.html
import lxml.etree
import requests
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup

data = {'text': 'test'}
web = requests.post('https://password.kaspersky.com/ru', data=data)
soup = BeautifulSoup(web.content, 'lxml')
#new_soup = soup.find({'class': 'description-block bad-score mt-lg-5 pb-2'})
for tag in soup.find_all('ul', {'class': 'score-description pb-4'}):
    print("{0}: {1}".format(tag.name, tag.text))


#tree = lxml.html.fromstring(web.text)
# elements = tree.find_class('description-block bad-score mt-lg-5 pb-2')
#elements = tree.xpath("//html/body/div[2]/div[2]/div[2]/div/h1")
#print(elements)
#/html/body/div[3]/div/div[3]/div[5]/ul/li[2] ПЛОХОЙ ВЫВОД
#/html/body/div[3]/div/div[3]/div[3]/ul/li[2] ХОРОШИЙ ВЫВОД
#elements = tree.xpath("//html/body/div[1]/div[2]/div[2]/div/h1")
# elements = tree.find_class('ul', {'class': 'score-description pb-4'})
#for el in elements:
#    print(el.text_content())

# print(web.content)
