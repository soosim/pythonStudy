# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

class mzitu(object):
	def all_url(self, url):
		html = self.request(url)
		all_a = BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
		for a in all_a:
			title = a.get_text()
			print('开始保存：', title)
			path = str(title).replace("?","_")
			self.mkdir(path)
			os.chdir(path)
			href = a['href']
			self.html(href)

	def html(self, hrel):
		html = self.request(href)
		max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
		for page in range(1, int(max_span) + 1):
			page_url = href + '/' + str(page)
			self.img(page_url)

	def img(self, page_url):
		img_url = self.request(page_url)
		img_url = BeautifulSoup(img_url.text, 'lxml').find('div', class_='main-image').find('img')['src']
		self.save(img_url)

	def save(self, img_url):
		name = img_url[-9:-4]
		img = self.request(img_url)
		f = open(name + '.jpg', 'ab')
		f.write(img.content)
		f.close()

	def mkdir(self, path):
		path = path.strip()
		isExists = os.path.exists(os.path.join("D:/mzitu", path))
		if not isExists:
			print('建立文件夹：', path)
			os.makedirs(os.path.join("D:/mzitu", path))
			return True
		else:
			print('文件夹' + path + '已存在')
			return False

	def request(self, url):
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
		content = requests.get(url, headers = headers)
		return content

	Mzitu = mzitu()
	Mzitu.all_url()