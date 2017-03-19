#! -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://mzitu.com/all'
start_html = requests.get(all_url, headers=headers)
html_file = 'C:/Users/soosim/Desktop/studyPy/1.html'

f = open(html_file,'w',encoding='utf-8')
f.write(start_html.text)
f.close()

soup = BeautifulSoup(open(html_file,'r',encoding='utf-8'), 'html.parser')

a_list = soup.find('div',attrs={'class':'all'}).find_all('a')

for a in a_list:
        title = a.get_text()
        path = str(title).strip()
        os.makedirs(os.path.join('D:/meitu',path))
        os.chdir('D:/meitu/'+path)
        href = a['href']
        html = requests.get(href, headers = headers)
        html_soup = BeautifulSoup(html.text,'html.parser')
        max_span = html_soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1,int(max_span)+1):
                page_url = href + '/' + str(page)
                img_html = requests.get(page_url, headers = headers)
                img_soup = BeautifulSoup(img_html.text,'html.parser')
                img_url = img_soup.find('div',class_='main-image').find('img')['src']
                name = img_url[-9:-4]
                img = requests.get(img_url, headers = headers)
                ff = open(name+'.jpg','ab')
                ff.write(img.content)
                ff.close()
                 

