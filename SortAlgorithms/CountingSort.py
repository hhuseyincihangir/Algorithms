#==============================================================================================#
#       title           :CountingSort.py                                                       #
#       description     :This program sorts by a sequence counting sort algorithm              #
#       author          :hashusfb                                                              #
#       contact         :hashusfb@gmail.com                                                    #
#       date            :20.10.2017                                                            #
#       python_version  :3.6                                                                   #
#       version         :0.1                                                                   #
#       version_notes   :                                                                      #
#==============================================================================================#

def getMax(array):
    n=len(array)
    mx=array[0]
    for i in range (0,n-1):
        if array[i]>mx:
            mx=array[i]
    return mx

def countingSort(array,maxValue):
    global steps
    steps=0
    n=len(array)
    m=maxValue+1
    count=[0]*m
    
    for a in array:
        count[a]+=1
        steps+=1
    i=0
    for a in range(m):
        for c in range(count[a]):
            steps+=1
            array[i]=a
            i += 1
    return array

if __name__=="__main__":
    arrayNumbers=[23,356,75,87,48,19,780,47,75,34,13,99]
    print("""
#####################################################################
    |                     Counting Sort                         | 
    |        Time Complexity          |     Space Complexity    |
    |  Worst  |   Best    |  Average  |           Worst         |
    |  O(n+k) |  Ω(n+k)   |   Θ(n+k)  |           O(k)          |
#####################################################################\n""")
    print("""Unsorted    : {}""".format(arrayNumbers))
    countingSort(arrayNumbers,getMax(arrayNumbers))
    print("""Sorted      : {}""".format(arrayNumbers))
    print("""Total Steps : {}""".format(str(steps)))