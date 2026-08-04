
# check every value in sequence 
# big o (n) 
# the time with increase with the number of enteries 


def linearSearch(l1,value):
    for i in range(len(l1)):
        if l1[i]==value:
            return i
        
    return -1
l1=[1,2,3,4,5,6,7,8,9,10,11,12]
l3=[2,3,3,3,3,3,4,5,5,5,6,6]
l2=[8]
position=linearSearch(l1,1) 

print(position)

