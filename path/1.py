# -*- coding:utf-8 -*-

import sys
import os


def formatSize(size):
    try:
        f_bytes = float(size)
        kb = f_bytes / 1024
    except:
        print('Wrong format of filesize')
        return 'Wrong format of filesize'
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        return "%fM" % M
    return "%fk" % kb

def getFileSize(filename):
    try:
        size = os.path.getsize(filename)
        return formatSize(size)
    except Exception as e:
        print(e)


if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

# 递归目录下文件
for i in os.walk(application_path):
    for filename in i[2]:

        # os.path.splitext 分离文件名与扩展名
        postfix = os.path.splitext(filename)[1]

        if postfix in ['.php','.avi','.mp4','.jpg']:
            full_name = os.path.join(i[0],filename)
            print(full_name + "---------" + getFileSize(full_name))



