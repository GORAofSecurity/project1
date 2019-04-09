#!/usr/bin/python
n = int(input())
ans=1
f0=0
f1=1

for n in range(1,n):
	ans=f1+f0
	f0=f1
	f1=ans
print(ans)    
