n=[8,9,3,1,2,0,5,0]        #Q1.add items from one list to the new list #Q2. Make two separate lists to show zeroes and numbers(adding if cond)
m=[]
zero=[]
for item in n:
    if item != 0:
        #print("num",item)
        m.append(item) #adding itmes from n[] to m[]
    else:
        zero.append(item)  
   
print('numbers :',m) #if print is inside the loop, every iteration steps will be displayed.Since we need the output in one line we're printing outside the loop 
print('zeroes :', zero)
