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


sen = input(f"Type the message to be shortened\n")


def algorithm1(sen):
    sen = list(sen)
    newSen = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    i = 1
    vowAddedCount = 0

    newSen = newSen + sen[0]
    if sen[0] in vowels:
        vowAddedCount += 1
    for i in range(1, len(sen)):
        if sen[i - 1] == " " and sen[i] in vowels:
            newSen = newSen + sen[i]
            vowAddedCount += 1
        if sen[i] != sen[i - 1] and sen[i] not in vowels:
            newSen = newSen + sen[i]

    dif = len(sen) - len(newSen)

    totalVowels = 0
    for i in range(len(sen)):
        if sen[i] in vowels:
            totalVowels += 1

    repCount = len(sen) - len(newSen) - (totalVowels - vowAddedCount)
    return f"\nAlgorithm 1\nVowels Removed: {totalVowels-vowAddedCount}\nRepeats Removed: {repCount}\nAlgorithm 1 message: {newSen.lower()}\nAlgorithm 1 characters saved: {dif}\n"


def algorithm2(sen):
    AltSen = list((str(sen)).replace(" ", "").lower())
    tempSen = ""
    finalSen = ""
    uniqueCharsCount = 0
    count = 0
    for i in range(len(AltSen)):
        if AltSen[i] not in tempSen:
            tempSen = tempSen + AltSen[i]
            uniqueCharsCount += 1

    for i in range(len(tempSen)):
        for j in range(len(AltSen)):
            if list(tempSen)[i] == AltSen[j]:
                count += 1
        finalSen = finalSen + str(count) + list(tempSen)[i]
        count = 0
    savedChar = len(sen) - len(finalSen)
    return f'Algorithm 2\nUnique characters found: {uniqueCharsCount}\nAlgorithm 2 message: {finalSen}\nAlgorithm 2 characters saved: {savedChar}'


print(algorithm1(sen))
print(algorithm2(sen))