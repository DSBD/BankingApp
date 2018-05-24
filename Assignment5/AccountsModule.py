from BankModule import Bank #Import the bank
import math #Import math class

class Accounts(): #Create accounts class
    def __init__(self, acctHolderName, acctNo, annualIntRate, balance, type): #Initialization method
        self._account = account #Assign the account variables

    def PredictBalance(account): #Predict Balance method will predict the balance after 12 months given the interest rate
        for i in range(len(Bank.accounts)):
            if(account == Bank.accounts[i][0]):
                initalBalance = Bank.accounts[i][2]
                percentRate = Bank.accounts[i][3]
                A = math.pow((1 + percentRate), 1)
                balanceWithInterest = initalBalance*A
                print("With Interest your new balance is ", balanceWithInterest)

    def CheckBalance(account): #Check balance method will return current balance
        for i in range(len(Bank.accounts)):
            if (account == Bank.accounts[i][0]):
                AccountBal = Bank.accounts[i][2]
                break
        print("The Balance of the account is: ", AccountBal)

    def deposit(account) : #Deposit method routes the deposit traffic given account type
        for i in range(len(Bank.accounts)):
            if (account == Bank.accounts[i][0]):
                if (Bank.accounts[i][4] == "c"):
                    ChequingAccounts.depositChequings(account)
                else:
                    SavingsAccounts.depositSavings(account)

    def withdraw(account): #Withdraw method routes the withdraw traffic given account type
        for i in range(len(Bank.accounts)):
            if (account == Bank.accounts[i][0]):
                if (Bank.accounts[i][4] == "c"):
                    ChequingAccounts.withrdrawChequings(account)
                else:
                    SavingsAccounts.withdrawSavings(account)
    

class ChequingAccounts(Accounts): #Chequing account class house specific methods for chequing accounts

    def depositChequings(account) : #Depsoit Methods deposits to chequing accounts
        for i in range(len(Bank.accounts)):
            if (account == Bank.accounts[i][0]):
                depositAmount = float(input("Enter the amount of money you would like to deposit: "))
                initalBalance = Bank.accounts[i][2]
                newBalance = initalBalance + depositAmount
                Bank.accounts[i][2] = newBalance
                print("Your new balance is ", Bank.accounts[i][2] ,"!")
    
    def withrdrawChequings(account): #Chequing Methods deposits to chequing accounts
        for i in range(len(Bank.accounts)):
            if (account == Bank.accounts[i][0]):
                withdrawAmount = float(input("Please Enter the amount you would like to withdraw: "))
                initialBalance = Bank.accounts[i][2]
                if(initialBalance - withdrawAmount >= -500):
                    newBalance = initialBalance - withdrawAmount
                    Bank.accounts[i][2] = newBalance
                    print("Your new balance is ", Bank.accounts[i][2] ,"!")
                else:
                    print("ERROR! Insuficient Funds")
    
class SavingsAccounts(Accounts): #Savings account class house specific methods for savings accounts

    def depositSavings(account) : #Depsoit Methods deposits to savings accounts
        for i in range(len(Bank.accounts)):
            if (account == Bank.accounts[i][0]):
                depositAmount = float(input("Enter the amount of money you would like to deposit: "))
                initalBalance = Bank.accounts[i][2]
                newBalance = initalBalance + depositAmount*1.5
                Bank.accounts[i][2] = newBalance
                print("Your new balance is ", Bank.accounts[i][2] ,"!")
    
    def withdrawSavings(account): #Withdraw Methods deposits to savings accounts
        for i in range(len(Bank.accounts)):
            if (account == Bank.accounts[i][0]):
                withdrawAmount = float(input("Please Enter the amount you would like to withdraw: "))
                initialBalance = Bank.accounts[i][2]
                if(initialBalance - withdrawAmount >= 0):
                    newBalance = initialBalance - withdrawAmount
                    Bank.accounts[i][2] = newBalance
                    print("Your new balance is ", Bank.accounts[i][2] ,"!")
                else:
                    print("ERROR! Insuficient Funds")