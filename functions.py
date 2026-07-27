

def sum_all(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

list1 = [4,4,4,4]
print(sum_all(*list1))
# print (sum_all(1,2,3,4,5))



def all_data(**kwargs):
    for keys , values in kwargs.items():
        print (f"keys : {keys} , values : { values}")


dict={
    "name": "areeba",
    "age":22,
    "salary":"JOBLESS"
}
# all_data(name="areeba", age=19, salary= "jobless")   
# all_data(**dict)  
all_data(**{
    "name": "areeba",
    "age":22,
    "salary":"JOBLESS"
})
