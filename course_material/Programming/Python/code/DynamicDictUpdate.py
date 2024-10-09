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

def split_dict_and_update(D):
    print("D:",D)
    D1=dict(list(D.items())[:int(len(D)/2)])
    D2=dict(list(D.items())[int(len(D)/2):])
    print("First half of D - D1:",D1)
    print("Second half of D - D2:",D2)
    splitkey=2
    splitvalue=D1[splitkey]
    D1[splitkey]=splitvalue[:int(len(splitvalue)/2)]
    D1[splitkey+1]=splitvalue[int(len(splitvalue)/2):]
    print("D1 after split:",D1)
    D2=dict([(k+1,v) for k,v in D2.items()])
    print("D2 after split:",D2)
    print("Merged D1 and D2:",D1|D2)

if __name__=="__main__":
    D={1:[1,2,3,4,5], 2:[5,6,7,8,9,10], 3:[3,4,5,6], 4:[6,1,2,3,4], 5:[4,5,2,1,1]}
    split_dict_and_update(D)
