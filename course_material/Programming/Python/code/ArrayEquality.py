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

def are_equal(array1,array2):
    if array1 == array2:
        print("arrays:",array1," and ",array2," are equal")
    else:
        print("arrays:",array1," and ",array2," are unequal")
    if array1.sort() == array2.sort():
        print("arrays:",array1," and ",array2," are equal after sorting")

if __name__=="__main__":
    are_equal([1,2,3,4,5],[3,2,1,5,4])
    are_equal([1,2,3,4,5],[1,2,3,4,5])
    are_equal(['a','b','c','d','e'],['b','c','d','a','e'])

