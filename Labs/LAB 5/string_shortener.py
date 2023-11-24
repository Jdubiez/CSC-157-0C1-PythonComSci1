#**************************************************************************
# * Name: Jahson Westby                                           CSC 157
# * Date: 11/20/23                                                  LAB 5   
# *************************************************************************
# * Problem Statement and Specifications: 
# * create 2 algorithms
# *
# * 1st: remove all vowles from sentance unless 
# * the vowel is the first or only letter
# * 
# * 2nd:  creates a string by taking each unique character in the 
# * message in the order they first appearand putting that letter 
# * and the number of times it appears
# * 
# * 
# * Input:  
# * This message could be a little shorter
# *
# * Output: 
# * Algorithm 1
# * Vowels removed: 11
# * Repeats removed: 2
# * Algorithm 1 message: ths msg cld b a ltl shrtr
# * Algorithm 1 characters saved: 13
# * Algorithm 2
# * Unique characters found: 15
# * Algorithm 2 message: 4t2h2i4s1m5e2a1g1c2o1u3l1d1b2r
# * Algorithm 2 characters saved: 8
# *
# *************************************************************************


string = (input(f"Type the message to be shortened\n"))

def algorithm1(string):
    string = list(string)
    newSen=[]
    i=0
    for i in len(string):
        if string[i].lower in ['a','e','i','o','u'] and string[i-1] == ' ':
            newSen.append(string[i])
            i+=1
            
        if string[i].lower in ['a','e','i','o','u']:
            i+=1
    return newSen   

print(algorithm1(string))


