# encoding: utf-8  
import os
import os.path
import sys
import chardet
import urllib
import time
#rootdir = 'E:'+os.sep+'sys.soolife.cn'+os.sep+'apps'+os.sep+'ads.sys.soolife.cn'+os.sep+'controllers'                                  # 指明被遍历的文件夹
#rootdir = 'E:'+os.sep+'v5.soolife.cn'+os.sep+'trunk'+os.sep+'api.soolife.cn'
config_name = 'check.py'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

rootdir = application_path

#获取脚本路径
#path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
# if os.path.isdir(path):
#     rootdir =  path
# elif os.path.isfile(path):
#     rootdir =  os.path.dirname(path)
    
#print rootdir
print 'please Waiting...'
a = 0
for i in os.walk(rootdir):
	for dirname in i[2]:
		postfix = os.path.splitext(dirname)[1]
		if postfix == ".php":
			path = os.path.join(i[0],dirname)
			f = open(path,"r")
			data = f.read()
			file_code = chardet.detect(data)['encoding']
			if file_code!='utf-8':
				a = 1
				f=open(rootdir+'/result.txt','a')
				f.write(path+'\n')
				f.close()
				#print dirname
if a==0:
	print'success! All file formats are for utf-8'
	time.sleep(2)
	exit(0)
print'Check completed, please in the result.txt file to see the results'
time.sleep(4)
exit(0)
