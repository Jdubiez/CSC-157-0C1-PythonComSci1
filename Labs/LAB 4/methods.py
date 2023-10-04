#**************************************************************************
# * Name: Jahson Westby                                             CSC 157
# * Date: 9/29/2023                                                   LAB 4   
# *************************************************************************
# * Problem Statement and Specifications: 
# * complete the functions
# * 
# * Input:  
# * a sentance, base height and character of rectangle,
# * number list, number list
# * Output: 
# * number of each vowel, rectangle, number of negatives and the negatives
# *
# *************************************************************************


# ****** COMPLETE THE FOLLOWING METHODS BELOW ******

# @param input a string   
# Precondition: input must be a non-empty string 
# Postcondition: display the input string, the number of characters in the input string, 
# as well as the counts for all vowel types in the input string. 

def display_vowel_info(input):

    aCount = (input.lower()).count('a')
    eCount = (input.lower()).count('e')
    iCount = (input.lower()).count('i')
    oCount = (input.lower()).count('o')
    uCount = (input.lower()).count('u')

    print (f'The sentence "{input}" has {len(input)} characters, and there are \n{aCount} a\'s \n{eCount} e\'s \n{iCount} i\'s \n{oCount} o\'s \n{uCount} u\'s')
        



# @params base the base length of the rectangle as a positive integer
#		  height the height of the rectangle as a positive integer
#         character the character used to print the rectangle  
# Precondition: base and height must be positive integers, character must be a valid
#				keyboard character
# Postcondition: prints the rectangle with dimensions base x height using the
# 				 specified character

def print_rectangle(base, height, character):
	
    for i in range(height):
        for j in range(base):
            print(character, end='')
        print()


    
      
# @params theList a list of numerical values
# @return the number of negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns number of negatives

def num_negatives(theList):
	
    negCount = 0

    for num in theList:
        if num < 0:
            negCount += 1
    
    return negCount

# @params theList a list of numerical values
# @return a list containing only the negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns a list of all negative numbers in the list

def negatives(theList):
    negatives = []

    for num in theList:
        if num < 0:
            negatives.append(str(num))
    return negatives
            



