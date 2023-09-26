#************************************************************************
# * Name: Your name                                                 CSC 157
# * Date: Today's date                                              LAB 0   
# *************************************************************************
# * Statement: Determine owner, selling cost and commission for house sale
# * Specifications:
# * Input  - owner
# *        - selling cost
# * Output - owner
# *        - selling cost
# *        - commission
# *************************************************************************


# output descriptive messages
print("This program calculates the cost to sell a home\n" 
                    + "and the commission paid to an individual sales agent.\n")

print("The user is asked for the last name of the seller and the\n" 
                    + "sales price.\n")

# prompt the user for input values

# seller's name
seller = input("Please enter the owner's last name: ")
# price of house
price = input("Please enter the sales price of the home: ")
        
# calculate the cost to sell the house and the commission
# on the sale of the listing and selling agents
cost = 0.06 * float(price)
commission = 0.015 * float(price)

# display the results
print( "\nThe " + seller + "'s home sold for $" + '{0:.2f}'.format(float(price)) )
print( "The cost to sell the home was $" + '{0:.2f}'.format(float(cost)) )
print( "The selling and listing agent earned $" + '{0:.2f}'.format(float(commission)) )





 
