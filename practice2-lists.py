num=[2,34,21,3,76,88,12,2,34]
print(num[2:])

print(num[-4]) #- index counts in reverse order

names=['Akshi','Naveen','Madhu','Prathi']
n=[num,names]
print(n)

num.remove(88)
print(num)

num.pop()
print(num)

del num[2:]
print(num)
num.extend([1,22,33,44])
print(num)

num.sort()
print(num)
