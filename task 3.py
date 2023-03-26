l=[1,2,3]

num=input('Give numbers to append to the list:')
num1=num.split(',')
for i in num1:
    o=int(i)
    l.append(o)
print(l)
