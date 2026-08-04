


# it runs for the best case scenerio aswell 
# if the list is sorted , the algo will still run 
# bubble sort / inserstion sort can stop early if the list is already sorted but selection sort cant 
# time complexity : (O(n²)) 


def SelectionSort(list1):


    lenth=len(list1)
    if lenth==0:
        return -1
    # small_index=None
    for i in range (lenth):
        # swapped=False

        small_index=i
        for  j in range (i+1,lenth):

            # print (f"i={i}, j={j} , small_index={small_index}")
            if list1[small_index]>list1[j]:
                # print(f"small:{small_index}, {list1[small_index] }> {list1[j]}")
                small_index=j
                # swapped=True

        if  small_index!=i:
            # print ("entered swapped")
            list1[i], list1[small_index] = list1[small_index], list1[i]
            # print (list1)



    return list1


emp_list=[]
list1=[1,8,2,4,9,2,3]
print(SelectionSort(list1))
print(SelectionSort(emp_list))
