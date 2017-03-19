#! -*- coding:utf-8 -*-
import time
import sys
import pymysql

# 获取当前时间
def getCurrentTime():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

def getCurrentDate():
	return time.strftime('%Y-%m-%d',time.localtime())

print(getCurrentTime())
print(getCurrentDate())

connection = pymysql.connect(host='qdm15474614.my3w.com',
							user='qdm15474614',
							password='soosim122927',
							db='qdm15474614_db',
							port=3306,
							charset='utf8')

try:
	with connection.cursor() as cursor:
		sql = "SELECT * FROM `we_textContents"
		cursor.execute(sql)
		res = cursor.fetchall()
		f = open('soosim_db.log','w')
		for row in res:
						print(row)
						f.write((str)(row[0]) +","+row[1] +","+(str)(row[2])+'\r\n')
		f.close()
except Exception as e:
	print(e)
else:
	pass
finally:
	print('End')
