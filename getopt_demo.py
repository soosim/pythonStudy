# -*- coding:utf-8 -*-
import getopt
import sys
import os

def usage():
	print("""
		Show help info:
			-a --addr address
			-p --port port
""")

if __name__ == '__main__':
	print(os.getcwd())
	opts,args = getopt.getopt(sys.argv[1:], "(Hh)a:p:",["help","addr=","port="])
	if opts:
		for o in opts:
			print(o)
	else:
		usage()
		sys.exit(0)