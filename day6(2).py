#TUPLES
names=("apple","mango","banana")
for n in names:
    print(n)
print(list(names))

m= ('o') 
print(m) #o/p is string

p=('o',) #tuple
print(p)

#assignment to remove duplicates
a=[1,3,6,7,10,10,1]
b= []

for item in a:
    if item not in b:  #if item is not in b,it'll append to it. if the no is already present it'll remove it
        b.append(item)

print(b)