#==============================================================================================#
#       title           :LinearSearch.py                                                       #
#       description     :This program searches through an array linear search algorithm        #
#       author          :Hasan Hüseyin CİHANGİR                                                #
#       contact         :hashusfb@gmail.com                                                    #
#       date            :20.10.2017                                                            #
#       python_version  :3.6                                                                   #
#       version         :0.1                                                                   #
#       version_notes   :                                                                      #
#==============================================================================================#

arrayNumbers=[2,0,5,7,8,9,0,7,5,4,3,9]
intendedNumber=4

def linearSearch(array,wanted):
    global find
    find=False
    for i in range(len(array)):
        if array[i]==wanted:
            find=True
            return i
if __name__=="__main__":
    print ("""
        ###   INFO    ###
    Array  : {}
    Wanted : {}
        ###  RESULTS  ###
    Index  : {}
    Find   : {}
    """.format(arrayNumbers,intendedNumber,linearSearch(arrayNumbers,intendedNumber),find))