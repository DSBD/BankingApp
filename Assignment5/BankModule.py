class Bank : #Class Header Defines Class
    accounts = [[100,"testUser1",100,3,"s"],[101,"testUser2",100,0.1,"c"],
                [102,"testUser3",100,3,"s"],[103,"testUser4",100,0.1,"c"],
                [104,"testUser5",100,3,"s"],[105,"testUser6",100,0.1,"c"], #Class List with Base accounts for testing
                [106,"testUser7",100,3,"s"],[107,"testUser8",100,0.1,"c"],
                [108,"testUser9",100,3,"s"],[109,"testUser0",100,0.1,"c"]]

    newaccount = [] #New account array will be used to store new account information for appention

    def __init__(self, accounts): #Initialize Bank
        self.accounts = accounts #Give the bank the accounts array as an asset

    def CreateAccount(clientName, acctNo, initBalance, interestRate, accountType): #This method recives all the information need for creation of a new account and creates and appends it to the array
        newaccount = [acctNo,(str(clientName)),initBalance,interestRate, accountType] #Collect all data in new account array
        Bank.accounts.append(newaccount) #Append new account to accounts list
        print("New Account ", newaccount[1], " with the Account number: ", newaccount[0], " has been created.") #Confirm creation of new accounts

    def getAccount(acctNo): #Get account method will forwards requests to the account class.
         if(choice == 1):
            Account.Account.getAccountBalence(accNo)
         elif(choice == 2):
            Account.Account.deposit(accNo)
         elif(choice == 3):
            Account.Account.withdraw(accNo)
         elif(choice == 4):
            Account.Account.predictBalence(accNo)
