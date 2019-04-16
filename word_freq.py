#!/usr/bash/python

import sys
import operator
dic = {}
check = 0
fname = sys.argv[1]
n=int(sys.argv[2])
with open(fname,"r") as f:
	lines = f.readlines()
	for IN in lines:
		IN = IN.split()
		for i in IN:
			if i in dic:
				dic[i] = dic[i]+1
			else:
				temp = {i:1}
				dic.update(temp)
	sorted_value =sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
	for(key,value) in sorted_value[0:n]:
		print "%-7s %7d" %(key,value)
