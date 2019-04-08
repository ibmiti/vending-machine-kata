def vendingMachine();  # creates the vending machine object
    count = 0          # defines the variable and gives it the value of 0, we will add to this later
    totalCredit = 0
    coinAmount = int(input("insert coins here: ")) 

 products = ["coca-cola":1.00,"chips":0.65,"candy":0.65]
 
# creating coin object's and giving them states
class penny
    value = 0.01
    weight = 2.5
    valid = True
    
class nickle
    value = 0.05
    weight = 5.0
    valid = True
class dime
    value = 0.10
    weight = 2.2
    valid = True
    
class quarter 
    value = 0.25
    weight = 5.6
    valid = True


# create list of valid coins and if not found invite them to insert valid coins
# then add inserted valid coins into totalCredit
validCoins = ["penny":True,"nickle":True,"dime":True,"quarter":True]
    while coin not in validCoins:
        print(int("insert valid coin: ")
    if coin in validCoins:
        totalCredit = count + coin + CoinAmount   

    
 print("You have ${0} in your bank.".format (round (totalCredit, 2)))   # rounding the int entered to the second decimal this will remove all 0's past the second decimal
    print("")
    print("Choose your item:")
    print("")
    print("1.Coca-Cola")
    print("2.chips")
    print("3.candy")
    print("")
    finalCredit = totalCredit
    round (finalCredit, 2)
    item = int (input ("Enter the number for your item: "))   # making the item equivalent to the number the user enters
    while item <1 or item >5:  # we have only 5 items, if the user enters an int that is higher than what we have specified then...
            print ("This item is not available.")  #this will print
            item = int (input ("Enter the number for your item: ")) # this will loop around as long as the user chooses the wrong item
    if item == 1:
        finalCredit = totalCredit - 1.00    # we are setting the price or each while at the same time deducting money from totalCredit
        print ("You now have a Coca- Cola can, costing $1.00.")
        print ("You have {0} remaining in your bank.".format (round(finalCredit,2))) #displaying the current value of totalCredit
    elif item = 2:
        finalCredit = totalCredit - 0.50
        print("You now have a bag of chips, costing 0.50")
        print("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    elif item = 3:
        finalCredit = totalCredit - 0.65
        print("You now have a bag of candy, costing 0.65")
        print("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    else:
        print ("This is not an option")
    print ("")
    print ("The rest of your money, ${0} has been outputted").format (round(finalCredit,2)))

    vendingMachine()


# if i had more time I would probably create a dictionary possibly with the ability to load new items via appending  and list comprehension to add more flexibility to my vending machine
