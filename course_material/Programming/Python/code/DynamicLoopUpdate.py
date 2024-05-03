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

def update_container_within_loop(iterable):
    if isinstance(iterable,list):
        cnt=0
        for i in iterable:
            iterable.pop(cnt)
            print(iterable)
            cnt+=1
    if isinstance(iterable,dict):
        for k1,v1 in iterable.items():
            for k2,v2 in v1.items():
                #multiplicand to array is equivalent to concatenation operator applied so many times (broadcast)
                iterable[k1][k2] = v2*2
                print(iterable)

if __name__=="__main__":
    update_container_within_loop([1,2,3,4,5,6,7,8,9,10])
    update_container_within_loop({'x1':{'y1':[1,2],'y2':[3,4]},'x2':{'y1':[5,6],'y2':[7,8]}})
