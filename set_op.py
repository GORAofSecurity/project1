#!/usr/bash/python

f_list=input("Please enter the first list:")
s_list=input("please enter the second list:")
f_list = f_list[1:len(f_list)-1]
s_list=s_list[1:len(s_list)-1]
f_list=f_list.split(',')
s_list=s_list.split(',')
union=[]
intersection=[]
count=0

union = list(first_list+s_list)

for i in f_list:
        for j in s_list:
                if int(i)==int(j):
                       	intersection.append(int(j))
       
union=list(set(union))
intersection=list(set(intersection))
union.sort()
intersection.sort()
print "intersection: ",intersection
print "union: ",union
