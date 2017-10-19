def bubbleSort(array):
    global steps
    steps=0
    n=len(array)
    for i in range(n):            
        for j in range(n-1-i):
            steps+=1
            if array[j]> array[j+1]:                
                inOrder=0
                array[j],array[j+1]=array[j+1],array[j]
if __name__=="__main__":
    print("""
#####################################################################
    |                       Bubble Sort                         | 
    |        Time Complexity          |     Space Complexity    |
    |  Worst  |   Best    |  Average  |           Worst         |
    |  O(n^2) |   Ω(n)    |   Θ(n^2)  |           O(1)          |
#####################################################################\n""")

    arrayNumbers=[23,356,75,87,48,19,780,47,75,34,13,99]   
    print("""Unsorted    : {}""".format(arrayNumbers))
    bubbleSort(arrayNumbers)
    print("""Sorted      : {}""".format(arrayNumbers))
    print("""Total Steps : {}""".format(str(steps)))