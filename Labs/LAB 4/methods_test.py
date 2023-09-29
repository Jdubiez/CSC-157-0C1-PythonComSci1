
# import methods
from methods import *

infoString = ('This program asks the user for a sentence,\n'
         'searches the sentence for all vowels,\n'
         'and displays the number of times each vowel appears in the sentence.\n')

print(infoString)
       
# prompt for input    
sentence = input('Enter a sentence: ')

display_vowel_info(sentence)

# prompt for input
base = int(input('Enter a positive integer for the base of the rectangle: ')) 
height = int(input('Enter a positive integer for the height of the rectangle: '))
character = (input('Enter a character used to print the rectangle: '))
print()

# print the rectangle by calling the printRectangle function
print_rectangle(base, height, character)
print()

# prompt the user to enter a list of numbers and store them in a list
list = [float(x) for x in input('Enter some numbers separated by whitespace ').split()]

print()    

# output the number of negatives    
print('The number of negatives in the list is', num_negatives(list))

# output the list of negatives numbers    
print('The negatives in the list are ', end = '') 
    
for items in negatives(list):
    print(items, ' ', sep = '', end = '') 
    
print('\n')


 
