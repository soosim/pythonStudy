# -*- coding:utf-8 -*-

import requests
import sys

# 帐号配置
account = [
		{'username':'aaaa','password':'123456'},
		{'username':'18671188982','password':'123456'},
		{'username':'15000675007','password':'123456'},
		{'username':'13593718021','password':'123456'},
		{'username':'13687215135','password':'123456'},
		{'username':'18772890422','password':'123456'},
		{'username':'13970158130','password':'123456'},
		{'username':'13593718260','password':'123456'},
		{'username':'13657193739','password':'123456'},
		{'username':'13636244121','password':'123456'},
		{'username':'13593738641','password':'123456'},
		{'username':'13477979221','password':'123456'},
		{'username':'18772990056','password':'123456'},
		{'username':'18238326201','password':'456789'}
	]

loginrul = "https://i.soolife.cn/m/login.html"
coinurl = "http://m.soolife.cn/life.html"
s = requests.session()

for member in account:
	s.post(loginrul, member)
	s.get(coinurl)
	print('Member '+ member['username'] + ' Success Gain The Coins')
