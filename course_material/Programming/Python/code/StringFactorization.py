from hyphen import Hyphenator

vowels={'a','e','i','o','u'}

def string_factorization(string):
    vowel_vector=[]
    consonant_vector=[]
    hyphenatedword=""
    hyphen=Hyphenator("en_US")
    syllables=hyphen.syllables(string)
    print("syllables:",syllables)
    for syllable in syllables:
        syllablelist=list(syllable)
        for n in range(len(syllablelist)):
            if syllablelist[n] in vowels:
                syllablelist[n]="-"
        hyphenatedword += "".join(syllablelist)
    print("Hyphenated word:",hyphenatedword)
    consonant_vector = hyphenatedword.split("-") 
    print("Consonant vector:",consonant_vector)
    vowelstr=""
    for n in range(len(hyphenatedword)):
        if hyphenatedword[n] == "-":
            vowelstr += string[n]
            continue
        vowel_vector.append(vowelstr)
        vowelstr=""
    print("Vowel vector:",vowel_vector)

if __name__=="__main__":
    string_factorization("concatenation")
