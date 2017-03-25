# -*- coding:utf-8 -*-

import sys
import os



class DirTools(object):
    '''
    目录、文件相关工具类
    '''
    def __init__(self, path):
        self.path = os.path.abspath(path)
        if not os.path.exists(self.path):
            raise Exception("File or Path '%s' is not exists" % path)

    def isFile(self):
        '''判断是否为文件'''
        return os.path.isfile(self.path)

    @staticmethod
    def formatSize(size=0, basis='h'):
        '''格式化输出文件大小'''
        f_bytes = float(size)
        kb = f_bytes / 1024
        if basis in ['h','H']:
            if kb >= 1024:
                M = kb / 1024
                if M >= 1024:
                    G = M / 1024
                    return (G,'g')
                return (M,'m')
            return (kb,'k')
        elif basis in ['k','K']:
            return (kb,'k')
        elif basis in ['m','M']:
            return (kb / 1024,'m')
        elif basis in ['g','G']:
            return (kb / 1024 / 1024,'g')

    def listFiles(self, suffix=None):
        '''列出目录下所有文件'''
        li = list()
        if self.isFile():
            li.append(self.path)
        else:
            # 递归目录下文件
            for i in os.walk(self.path):
                for filename in i[2]:
                    full_name = os.path.join(i[0],filename)
                    if suffix:
                        # os.path.splitext 分离文件名与扩展名
                        postfix = os.path.splitext(filename)[1]
                        if isinstance(suffix,list):
                            if postfix in suffix:
                                li.append(full_name)
                        elif isinstance(suffix,str):
                            if postfix is suffix:
                                li.append(full_name)
                    else:
                        li.append(full_name)
        return li
                
    def getSize(self):
        '''获得文件或者目录大小'''
        if self.isFile():
            return os.path.getsize(self.path)
        else:
            size = 0
            for root, dirs, files in os.walk(self.path):
                size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
            return size

if __name__ == '__main__':
    try:
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        tool = DirTools(application_path)
        res = tool.getSize()
        # res = tool.listFiles(suffix = '.md')
        print(DirTools.formatSize(res))
    except Exception as e:
        print(e)
    finally:
        print('The End')

