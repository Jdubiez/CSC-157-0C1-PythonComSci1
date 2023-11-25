# **************************************************************************
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

#get user input
sen = input(f"Type the message to be shortened\n")

#first function
def algorithm1(sen):
    #convert input to list
    sen = list(sen)
    
    #variables
    newSen = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    i = 1
    vowAddedCount = 0
    totalVowels = 0


    #first letter should always be printed
    newSen = newSen + sen[0]

    #checking if first letter is vowel so it can be added to vowel count
    if sen[0] in vowels:
        vowAddedCount += 1

    #loop looking for words that start with a vowel
    for i in range(1, len(sen)):
        if sen[i - 1] == " " and sen[i] in vowels:
            newSen = newSen + sen[i]
            vowAddedCount += 1

        #looking for duplicate letters and if letter is a vowel
        if sen[i] != sen[i - 1] and sen[i] not in vowels:
            newSen = newSen + sen[i]

    #characters savved is just the difference between the final and inital sentence
    dif = len(sen) - len(newSen)

    #loop counting the total vowels in teh sentence
    for i in range(len(sen)):
        if sen[i] in vowels:
            totalVowels += 1

    #repeated letters can be found by subtracting everything from the initial sentence
    repCount = len(sen) - len(newSen) - (totalVowels - vowAddedCount)

    #formatting everything
    return f"\nAlgorithm 1\nVowels removed: {totalVowels-vowAddedCount}\nRepeats removed: {repCount}\nAlgorithm 1 message: {str(newSen).lower()}\nAlgorithm 1 characters saved: {dif}\n"

#second function
def algorithm2(sen):

    #turning string into lowercase list without spaces
    AltSen = list((str(sen)).replace(" ", "").lower())

    #other variables
    tempSen = ""
    finalSen = ""
    uniqueCharsCount = 0
    count = 0

    #loop making a new sentence with only unique characters and counting how many unique characters there are
    for i in range(len(AltSen)):
        if AltSen[i] not in tempSen:
            tempSen = tempSen + AltSen[i]
            uniqueCharsCount += 1

    
    for i in range(len(tempSen)):
        for j in range(len(AltSen)):
            #checking to see how many times each letter appears and counting it
            if list(tempSen)[i] == AltSen[j]:
                count += 1
        finalSen = finalSen + str(count) + list(tempSen)[i]
        count = 0
    savedChar = len(sen) - len(finalSen)

    #formatting
    return f'Algorithm 2\nUnique characters found: {uniqueCharsCount}\nAlgorithm 2 message: {finalSen}\nAlgorithm 2 characters saved: {savedChar}'

#printing both algorithms
print(algorithm1(sen))
print(algorithm2(sen))