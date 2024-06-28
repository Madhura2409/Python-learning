def addition(a,b,c):
    d= a + b + c
    print("Output1:",d)
    
addition(10,20,30) 

def name(val):
    print("Output2:",val)
a = (20,10,4) 
name(a) 

def name(val):
    print("Output3.1:",val) 
    a,b,c = val #calling val into a,b,c
    print ("Output3.2:",a,b,c)
    x = a+b-c
    print("Output3.3:",x)
#a = (20,10,4) 
name((20,10,4)) 
name([20,10,4]) 
name({20,10,4}) 
#name({"Hi":20,"Hello":10,"Bye":4}) #will not work for x=a+b+c because its addition of nos





    
