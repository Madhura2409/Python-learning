class Company:
    def __init__(self):
        print("Class started")
    def hi(self,msg):
        print(msg)
c = Company()
#c.hi()

c1 = Company()

c2 = Company()    #objs c,c1,c2 are calling the same class
c.hi("hi")
c1.hi("hi")

c2.hi('hi')       #similarly c,c1,c2 are calling the same func