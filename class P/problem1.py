class A():
    def addition(self,a,b):
        c=a+b
        print(c)

class B(A):
    def Multi(self,c,p):
        y=c*p
        print(y) 

object=B()  
object.addition(67,90)
object.Multi(67,90)         
        