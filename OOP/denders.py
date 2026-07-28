class Complex :
    # real=None
    # imaginary=None
    def __init__(self, real,img):
        self.real=real
        self.img=img

    def __add__(self, other): # now it will automatically call when "+" is used with complex class objects 
        real=self.real+other.real
        img=self.img+other.img
        return Complex(real,img)
    def __str__(self):# returns the string representation of an object istead of its address so whenever a simple object is being printed it will print the string form 
        return (f"real: {self.real} imaginary : {self.img}")

    def __mul__(self, other):
        real=self.real*other.real
        img=self.img*other.img
        return Complex(real,img)
    def __eq__(self, other):
        return self.real==other.real and self.img==other.img


c1=Complex(2,3)
c2=Complex(3,4)

# print(c1+c2)
c_mul=c1*c2
c=c1+c2
print(c)
print(c_mul)

print (c1==c2)
