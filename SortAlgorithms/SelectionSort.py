#==============================================================================================#
#       title           :SelectionSort.py                                                      #
#       description     :This program sorts by a sequence selection sort algorithm             #
#       author          :Hasan Hüseyin CİHANGİR                                                #
#       contact         :hashusfb@gmail.com                                                    #
#       date            :20.10.2017                                                            #
#       python_version  :3.6                                                                   #
#       version         :0.1                                                                   #
#       version_notes   :                                                                      #
#==============================================================================================#

def selectionSort(array):
    global steps
    steps=0
    temp=0
    minimum=0
    n=len(array)
    for i in range(0,n):
        minimum=i
        for j in range(i,n):
            steps+=1
            if array[j] < array[minimum]:
                minimum=j
        temp=array[i]
        array[i]=array[minimum]
        array[minimum]=temp
    return array
if __name__=="__main__":
    arrayNumbers=[23,356,75,87,48,19,780,47,75,34,13,99]
    print("""
#####################################################################
    |                     Selection Sort                        | 
    |        Time Complexity          |     Space Complexity    |
    |  Worst  |   Best    |  Average  |           Worst         |
    |  O(n^2) |  Ω(n^2)   |   Θ(n^2)  |           O(1)          |
#####################################################################\n""")
    print("""Unsorted    : {}""".format(arrayNumbers))
    selectionSort(arrayNumbers)
    print("""Sorted      : {}""".format(arrayNumbers))
    print("""Total Steps : {}""".format(str(steps)))