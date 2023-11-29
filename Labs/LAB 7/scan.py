#**************************************************************************
# * Name: Jahson Westby                                            CSC 157
# * Date: 11/29/23                                                   LAB 7   
# *************************************************************************
# * Problem Statement and Specifications: 
# * read given file and output the items, price, total cost, and total items
# * 
# * Input:  
# * given files
# *
# * Output: 
# * items, price, total cost, total items
# *
# *************************************************************************

# output descriptive messages
print('This program will read each line in the file invoice.txt and print a\n'
       + 'a table indicating the item and it\'s cost.  When the file is exhausted,\n'
       + 'it will print the cumulative sum of all of the costs and the total \n'
       + 'number of items.\n')

# display header line for items list
print('{0: <10}'.format('Item'), '{0: >17}'.format('Cost'), sep = '' )

# add your remaining code below

prices = []
items = []
text = open('invoice.txt', 'r')

for line in text:

       item, price = line.split('#')
       items.append(item)
       prices.append(price.strip())

prices = [float(i) for i in prices]

for i in range(len(items)):
       print('{0: <10}'.format(items[i]), '{0: >17}'.format(f'${"{:.2f}".format(prices[i])}'), sep = '' )

print()
print('{0: <10}'.format('Total cost:'), '{0: >16}'.format(f'${"{:.2f}".format(sum(prices))}'), sep='')
print('{0: <10}'.format('Number of tools:'), '{0: >11}'.format(len(items)), sep='')

