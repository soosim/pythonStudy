# -*- coding:utf-8 -*-

import sys
import os.path
import chardet
import getopt

def usage():
    notice ='''
Param list:
    -f --file file name or path name    
    '''
    print(notice)


def check():
    try:
        options,args = getopt.getopt(sys.argv[1:],"f:",["file="])
        print(options)
        print(args)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    check()
