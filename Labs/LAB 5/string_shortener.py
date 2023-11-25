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

def algorithm1(sen):

    sen = list(sen)
    newSen= ''
    vowels= ['a','e','i','o','u','A','E','I','O','U']
    i=1
    vowAddedCount = 0
    
    newSen= newSen+sen[0]
    if sen[0] in vowels:
        vowAddedCount+=1
    for i in range(1,len(sen)):
        if sen[i-1] == ' ' and sen[i] in vowels:
            newSen= newSen+sen[i]
            vowAddedCount += 1
        if sen[i] != sen[i-1] and sen[i] not in vowels:
            newSen= newSen+sen[i]
            
    dif=len(string) - len(newSen)

    totalVowels = 0
    for i in range(len(string)):
        if string[i] in vowels:
            totalVowels+=1
    
    repCount = len(sen)- len(newSen) - (totalVowels-vowAddedCount)
    return f'\nAlgorithm 1\nVowels Removed: {totalVowels-vowAddedCount}\nRepeats Removed: {repCount}\nAlgorithm 1 message: {newSen.lower()}\nAlgorithm 1 characters saved: {dif}\n'

print(algorithm1(string))


