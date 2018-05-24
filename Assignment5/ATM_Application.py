from BankModule import Bank #Import the bank
from AccountsModule import Accounts #Import the 

class ATMApplication (Bank, Accounts) :#Create the ATM Application class
    
    def __init__(): #Init does nothing in this class
        pass

    def run(): #Run method houses main code

        ATMApplication.Menu1() #Display Menu

        while True : #Loop allows program to run until the user chooses to exit
            choice = int(input("\nEnter a choice: ")) #Take choice from user
            
            if choice == 1 : #Select Account
                while True:#While loop for error checking
                    acctNo = int(input("Enter an Client number: ")) #Prompt user to enter accout number
                    i = 0 #Start i at 0
                    for i in range (len(Bank.accounts)) :#Run for loop to find account
                        error = True #Initialize error to true
                        if (acctNo == Bank.accounts[i][0]) : #If account is found
                            error = False #Set error to false
                            break #Break for loop
                    if error == True : #If errored
                        print("\nAccount Number does not exist!\n") #Display account message
                    else : #Else
                        break #End Applicaion
                ATMApplication.SelectAccount(acctNo) #Call select account method
                continue 
            
            elif choice == 2 : #Create Account
                clientName = str(input("Enter Your Name: ")) #Propmt user to enter name
                while True: #While loop for error checking
                    acctNo = int(input("Enter a Client Number: ")) #Prompt user to enter account number
                    i = 1 #The following code checks to see if the account already exists with that number
                    for i in range (len(Bank.accounts)) :
                        error = False
                        if (acctNo == Bank.accounts[i][0]) :
                            error = True
                            break
                    accountType = str(input("Enter Account Type (c:chequing/s:savings): ")) #Prompt user to enter account type
                    initBalance = float(input("Enter your initial account balance: ")) #Prompt user to enter initial balance
                    interestRate = float(input("Enter your interest Rate: ")) #Prompt user to enter interest rate
                    if(accountType == "s"): #If account is savings verify that the interest rate is above 3%, if not prompt for re entry
                        while(interestRate < 3.0):
                            interestRate = float(input("INVALID Interest Rate. Enter new interest Rate: "))
                    else: #If account is chequing verify that the interest rate is below 1%, if not prompt for re entry
                        while(interestRate > 1.0):
                            interestRate = float(input("INVALID Interest Rate. Enter new interest Rate: "))
                    if error == True : #If an error occured inform the user
                        print("\nInvalid Account number; this number is in use!\n")
                    elif acctNo < 100 : #If the account number is invalid prompt the user
                        print("\nInvalid Number!\n")
                    else : #Else End
                        break 
                Bank.CreateAccount(clientName,acctNo, initBalance, interestRate, accountType) #Create the new bank accout
                ATMApplication.Menu1() #Run the second menu
                continue 

            elif choice == 3 : #Quit
                quit()
            
            else : #Error Checking
                print("\nInvalid Choice! ")
                continue

    def SelectAccount(acctNo): #Select account will allow the verious choices to be used
        
        ATMApplication.Menu2() #Run second menu
        
        while True : #Loop allows user to continue until they choose to exit
            choice2 = str(input("\nEnter a choice: "))
            if choice2 == "a" :
                Accounts.CheckBalance(acctNo)
            elif choice2 == "b" :
                Accounts.deposit(acctNo)
            elif choice2 == "c" :
                Accounts.withdraw(acctNo) 
            elif choice2 == "d" :
                Accounts.PredictBalance(acctNo)
            elif choice2 == "e" :
                print()
                ATMApplication.Menu1()
                break
            else :
                print("\nInvalid Choice! ")
                continue

    def Menu1(): #First Menu
        print("\nMain Menu")
        print("\n1: Select Account")
        print("2: Create Account")
        print("3: Exit")
    
    def Menu2(): #Second Menu
        print("\na. Check Balance")
        print("b. Deposit")
        print("c. Withdraw")
        print("d. Predict Balance")
        print("e. Exit Account")