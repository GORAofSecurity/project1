#!/usr/bin/python
number = input()
for i in number:
        if i != '0' and i != '1':
                print("invalid Input")
                exit(0)
binary = (list(num))
length = len(binary)
plus = 4 - length % 4
tmp =[]
for i in range(0,plus)
        tmp.append( '0' )
binary = tmp + binary
length = len(binary)
thing = 4 - ((length/4)%4)
zero = ['0','0','0','0']
for i in range(0,thing):
        binary = zero + binary
length = (len(binary)/4)
decimal = []
string = ''
result = ''
for i in range(0,length):
        for j in  range(0,4):
                decimal.append(int(binary[i*4+j]))
                string = string + str(binary[i*4+j)
        result = result + ("%x" % (int(string,2)))
        if (i+1)%4==0 :
                result = result + ' '
        del(decimal[0:4])
        string = ''
print(result)

