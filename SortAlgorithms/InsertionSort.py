
def insertionSort(array):
    n=len(array)

    for i in range(0,n):
        key=array[i]
        j=i-1
        while (j>=0) and (array[j]>key):
            array[j+1] = array[j]
            j -=1
        array[j+1]=key

if __name__=="__main__":
    arrayNumbers=[2,0,5,7,8,9,0,7,5,4,3,9]
    print ("""Unsorted: {} """.format(arrayNumbers))
    insertionSort(arrayNumbers)
    print ("""Sorted  : {} """.format(arrayNumbers))