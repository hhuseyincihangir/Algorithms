
arrayNumbers=[2,0,5,7,8,9,0,7,5,4,3,9]
intendedNumber=4

def lineerSearch(array,wanted):
    global status
    status=False
    for i in range(len(array)):
        if array[i]==wanted:
            status=True
            return i

print ("""
    ###   INFO    ###
Array  : {}
Wanted : {}
    ###  RESULTS  ###
Status : {}
Index  : {}
""".format(arrayNumbers,intendedNumber,lineerSearch(arrayNumbers,intendedNumber),status))