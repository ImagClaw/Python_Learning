#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Use the Account class to simulatean ATM machine. Create ten accounts in a list with the ids 
#               0, 1, ..., 9, and an initialbalance of $100. The system prompts the user to enter an id. If 
#               the id is enteredincorrectly, ask the user to enter a correct id. Once an id is accepted, 
#               the mainmenu is displayed as shown in the sample run. You can enter a choice of 1 forviewing 
#               the current balance, 2 for withdrawing money, 3 for depositing money,and 4 for exiting the 
#               main menu.
#   Date:5/13/2019


class Account:
    def __init__(self, id = 0, balance = 100):
    	self.__id = id
    	self.__balance = balance

    def setId(self, id):
    	self.__id = id

    def setBalance(self, balance):
    	self.__balance = balance

    def withdraw(self, amount):
    	if self.__balance >= amount:
    		self.__balance -= amount

    def deposit(self, amount):
    	self.__balance += amount

    def getId(self):
    	return self.__id

    def getBalance(self):
    	return self.__balance
        
    def mainMenu(self):
        return "Main menu \n1: Check balance \n2: Withdraw \n3: Deposit \n4: Exit"
    

def main():
    for i in range (10):
        accountlist = []
        accountlist.append(Account(id=i))

    idInput = int(input("Input your ID: "))
    if idInput > 10:
        print("Account doesn't exist")
        return 0

    newatm = Account(idInput)
    while True:
        print(newatm.mainMenu())
        choiceInput = int(input("Enter a choice: " ))
        if choiceInput == 1:
            print("\n\tBalance is: ${:.2f}".format(newatm.getBalance()))
        elif choiceInput == 2:
            d = int(input("Enter amount to withdraw: "))
            newatm.withdraw(d)
            print("\n\t New Balance ${:.2f}".format(newatm.getBalance()))
        elif choiceInput == 3:
            d = int(input("\nEnter amount to withdraw: "))
            newatm.deposit(d)
            print("\n\t New Balance ${:.2f}".format(newatm.getBalance()))
        elif choiceInput == 4:
            break

if __name__ == "__main__":
    main()