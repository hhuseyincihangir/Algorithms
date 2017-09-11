
arrayNumbers=[2,0,5,7,8,9,0,7,5,4,3,9]

print("""Unsorted: {}""".format(arrayNumbers))

def selectionSort(array):
    temp=0
    minimum=0
    n=len(array)
    for i in range(0,n):
        minimum=i

        for j in range(i,n):
            if array[j] < array[minimum]:
                minimum=j
        temp=array[i]
        array[i]=array[minimum]
        array[minimum]=temp
    return array

print("""Sorted  : {}""".format(selectionSort(arrayNumbers)))