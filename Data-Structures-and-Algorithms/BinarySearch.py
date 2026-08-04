#check on  the midpoint ,if value found return 
# if the required value is greater than mid value then move on right side and find the mid value again 
# if the req value is less than mid value move on left side and find mid value agian 

#time complexity : BIg O (log n )
# space complexity : in-place sorting / constant space complx


def binary_search(list1,num):

    last=len(list1)
    start=0
    while True:
        mid=(start+last)//2
        print(mid)
        if (list1[mid]==num):
            position=mid
            return position
        elif (num>list1[mid]):
            start=mid+1
        elif(num<list1[mid]):
            last=mid-1
        return -1


l1=[1,2,3,4,5,6,7,8,9,10,11,12]
l3=[2,3,3,3,3,3,4,5,5,5,6,6]
l2=[8]
position=binary_search(l3,1) 

print(position)






    
