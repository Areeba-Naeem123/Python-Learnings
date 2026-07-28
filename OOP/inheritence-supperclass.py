class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def printTwoD(self):
        print(f"the vector is {self.i}i+{self.j}j")

class ThreeDvector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def printThreeD(self):
        print(f"the vector is \n{self.i}i+ {self.j}j+ {self.k}k")


v=ThreeDvector(2,3,4)
v.printThreeD()
