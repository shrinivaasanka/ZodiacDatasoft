##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io
##############################################################################################################################################

import numpy
from collections import defaultdict


def mixed_python_arrays(remove="simulated"):
    dictionary = defaultdict(list)
    ndarr1 = numpy.int32([[[1, 2]], [[11, 12]]])
    ndarr2 = numpy.int32([[[4, 5]]])
    ndarr3 = numpy.int32([[[7, 8]]])
    ndarr4 = numpy.int32([[[10, 11]]])
    ndarr5 = numpy.int32([[[13, 14]]])
    dictionary[0] = [[100, 200], ndarr1, ndarr2, ndarr3, ndarr4, ndarr5]
    print("dictionary before remove:", dictionary)
    print("ndarr1==dictionary[0][0]:", ndarr1 == dictionary[0][0])
    print("ndarr1==dictionary[0][1]:", ndarr1 == dictionary[0][1])
    print("ndarr1==dictionary[0][2]:", ndarr1 == dictionary[0][2])
    print("ndarr1==dictionary[0][3]:", ndarr1 == dictionary[0][3])
    print("ndarr1==dictionary[0][4]:", ndarr1 == dictionary[0][4])
    print("ndarr1==dictionary[0][5]:", ndarr1 == dictionary[0][5])
    if remove == "remove":
        try:
            dictionary[0].remove(ndarr1)
        except Exception as ex:
            print("exception:", ex)
    if remove == "simulated":
        # temp=[]
        # for e in dictionary[0]:
        #    if (e==ndarr1)[0][0][0] == False:
        #        temp.append(e)
        #    else:
        #        print("excluding element to be removed from copy:",e)
        # dictionary[0]=temp
        dictionary[0] = [x for x in dictionary[0]
                         if (x == ndarr1)[0][0][0] == False]
    print("dictionary after remove:", dictionary)


if __name__ == "__main__":
    print("==========Remove (doesn't work) ===========")
    mixed_python_arrays(remove="remove")
    print("==========Simulated Remove by excluded copy (works) ===========")
    mixed_python_arrays(remove="simulated")
