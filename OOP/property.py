class Employee:
    salary =5000
    increment=10
    
    @property
    def salary_increment(self):
        return (self.salary+self.salary*(self.increment/100))
    @salary_increment.setter
    def salary_increment(self,salary):
        self.increment=((salary/self.salary)-1)*100


e=Employee()
print(e.salary_increment)

e.salary_increment=15000
print(e.salary_increment)

    
