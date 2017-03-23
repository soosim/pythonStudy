# -*- coding: utf-8 -*-

import chardet

file = './1.php'
fp = open(file,'r')
content = fp.read()
#print(chardet.detect(content))
print(content)
