
# compare adjacent values 
# move the greater value on the right side 
# the inner loop will iterate less everytime 
# inner loop will not iterate the end values which are being sorte already 
# it is confirm that after the first iteration the end value (largest) is sorted 
# time complexity : n(n-1)=n^2
#space complexity : in - place sorting / constant complexity 





def BubbleSort(list1):
    swapped=False
    length_list=len(list1)
    for i in range (length_list-1):
        for j in range(length_list-1-i):
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
                swapped=True

        if not swapped:
            break

    return list1



list1=[1,8,2,4,9,2,3]
print(BubbleSort(list1))

