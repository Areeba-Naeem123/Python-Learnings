
#If the list is already sorted, Insertion Sort is very fast. This is why it's often preferred over 
# Selection Sort for nearly sorted data.
# best case scenerio : while loop will not run 
# best case : time complexity : big O(n)
# worst case scenerio : big O (n^2)


def insertionSort(list1):
    length=len(list1)
    if length==0:
        return -1
    for i in range(1,length):
        j=i-1
        current=list1[i]
        while j>=0 and list1[j]>current:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=current
    return list1

list1=[2,8,1,3]
list2=[]
print(insertionSort(list1))
print(insertionSort(list2))




