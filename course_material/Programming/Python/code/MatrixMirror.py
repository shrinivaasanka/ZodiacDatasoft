import numpy as np

def matrix_mirror(strings):
    string_matrix=[]
    for s in strings:
        srow = list(s)
        string_matrix.append(srow)
    print("Strings:",strings)
    string_matrix_nd=np.asarray(string_matrix)
    string_matrix_nd=np.fliplr(string_matrix_nd)
    for r in string_matrix_nd:
        print("Mirrored string:","".join(r))

if __name__=="__main__":
    matrix_mirror(["abcde","fghij","klmno","pqrst","uvwxy"])
    matrix_mirror(["#############",
                   "#---------###",
                   "##--#####--##",
                   "##--#####--##",
                   "##--#####--##",
                   "##--#####--##",
                   "#---------###",
                   "#############"])
