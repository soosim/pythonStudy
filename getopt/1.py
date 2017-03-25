# -*- coding:utf-8 -*-

import sys
import os.path
import os
import getopt

p = os.path.dirname(__file__)

ops,aaa = getopt.getopt(sys.argv[1:], "o:a")

a = input('Enter options : ')
print(a)

input("Print any key to exit : ")
exit(0)
print(ops,aaa)
