def insertionSort(array):
    global steps
    steps=0
    n=len(array)
    for i in range(0,n):
        key=array[i]
        j=i-1
        while (j>=0) and (array[j]>key):
            steps+=1
            array[j+1] = array[j]
            j -=1
        array[j+1]=key

if __name__=="__main__":
    arrayNumbers=[23,356,75,87,48,19,780,47,75,34,13,99]
    print("""
#####################################################################
    |                     Insertion Sort                        | 
    |        Time Complexity          |     Space Complexity    |
    |  Worst  |   Best    |  Average  |           Worst         |
    |  O(n^2) |   Ω(n)    |   Θ(n^2)  |           O(1)          |
#####################################################################\n""")
    print("""Unsorted    : {}""".format(arrayNumbers))
    insertionSort(arrayNumbers)
    print("""Sorted      : {}""".format(arrayNumbers))
    print("""Total Steps : {}""".format(str(steps)))