"""


 Objective :
 Write a Python program that simulates an Automatic Teller Machine (ATM).
 Do not import libraries


Requirements:

- Write your algorithm first
- Should use Python classes
- Should ask the user of your program for user ID and a PIN number
- Should have some fake accounts and holders directly into the program, with
starting balances (using dictionary), The user should able to check the balance
of, withdraw from, or deposit into their checking account
- Should have a main() function that uses any classes you wrote in some sort of
interactive loop
- Once you are done, let's share the solution on Slack

"""

#create a dictionary of staged user information
#checking number
#savings number
#pin number
#checking balance
#savings balance
#name

#class
#print grettings
#ask user what they want to do
#central loop that farms out to the other methods

#check balance method
#asks for checking or savings or all
#prints balances, leaves

#deposit method
#asks for checking or savings
#prints balance
#accepts users deposit
#adds to balance
#place holder for actual transaction calls
#prints ending balances, leaves

#withdrawl method
#ask for checking or savings
#prints balance
#accepts users withdrawl amount
#subtracts withdrawl from balance
#place holder for actual transaction
#prints remaining balances, leaves

#transfer method
#ask from-to checking versus savings
#prints balances available
#accepts user transfer amount
#subtract from one account, add to the other
#prints new balances, leaves

class AutomatedTransactionMachine:
    def __init__(self):
        user_name = ""
        savings_account = int
        checking_account = int
        savings_balance = float
        checking_balance = float
        pin = int
        self.client_dict = {
             101:
                 {
                 user_name: "Erin Church",
                 savings_account: 501,
                 checking_account: 601,
                 savings_balance: 5000.0,
                 checking_balance: 6000.0,
                 pin: 1234
                 },

            102:
                {
                user_name: "Ronald Williams",
                savings_account: 502,
                checking_account: 602,
                savings_balance: 4500.0,
                checking_balance: 5500.0,
                pin: 4321
                },

        }


    def start(self):
        choice = ""
        confirmed = bool
        print("Welcome to Bank of Erin.\t")
        print("We appreciate your business.\t")
        self.confirm_account()
        if confirmed == True:
            print("How can we help you today?\t")
            print("To Check Balance: C.\n To Withdrawal Funds: W.\nTo Deposit Funds: D.\n To Transfer Funds: T.\n To finish and exit: Exit.")
            values_check_balance = ["C", "c", "check", "Check Balance", "Check", 'check balance']
            values_deposit_funds = ["D", "d", "deposit", "Deposit Funds", "Deposit", 'deposit funds']
            values_withdrawal_funds = ["w", "W", "withdrawal", "withdrawal funds", "Withdrawal", 'Withdrawal Funds']
            values_transfer_funds = ["T", "t", "transfer", "Transfer", "Transfer Funds", 'transfer funds']
            values_exit = ["E", 'e', 'exit', 'Exit']



    def confirm_account(self):
        client_id = 0
        pin_number = 0
        client_id = int(input("Please enter your client ID.\t"))
        pin_number = int(input("Please enter your pin number.\t"))
        confirmed = bool
        self.client_dict()

        if client_id in client_dict():
            if pin_number in client_dict.values():
                confirmed = True
            else:
                print("Client could not be confirmed.\t")
                confirmed = False
        else:
            print("Client account does not exist, please see a teller.\t")
        return confirmed


    def check_balance(self):
        print('Erin to write check balance method')
        pass

    def deposit(self):
        print('Erin to write deposit funds method')
        pass

    def withdrawal(self):
        print('Erin to write the withdrawal funds method')
        pass

    def transfer(self):
        print('Erin to write the transfer funds method')
        pass

def  main():
    me = AutomatedTransactionMachine()
    me.start()

if __name__ == "__main__":
    main()
