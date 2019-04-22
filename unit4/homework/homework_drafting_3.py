#THIS WEEK

"""
TO DO: (UNIT 4)

ADD TRY/EXCEPT

ADD *ARGS OR **KWARGS, TURN RESPONSES FROM METHODS INTO DICTIONARIES

CREAT 3 CLASSES FOR PROFILES
- CLIENT ATM (ALREADY HAVE FUNCTIONALITY IN MAIN, JUST MOVE THAT UP, MAYBE CONFIRM USER NAME FIRST?
- BANK (DO YOU NEED TO CONFIRM IDENTITY? MAYBE A LITTLE - MAYBE CONFIRM USER NAME AND PASSWORD?
- TELLER MAYBE CONFIRM USER NAME AND PASSWORD AND ACCOUNT INSTEAD OF PIN

TO DO: (UNIT 5)

INSTEAD OF WRITING AND DICTIONARIES IN INIT
- MOVE DICTIONARIES TO FILES
- MOVE WRITING OF TRANSACTIONS TO FILES
- DECIDED WHETHER OR NOT TO WRITE TO SCREEN

"""

# from previous week keep basic functionality of atm

#add try/catch for errors


#create 3 classes for profiles, the bank, the teller, and the customer via atm

#what is in main at the moment is the customer via atm

#the teller would only need to confirm accounts, not pin numbers, maybe they see the before and after balances for transfers

#the bank is very similar to the teller maybe just the input is different?

#look into the #args and the #kwargs? didn't figure out how to use those


"""
PSEUDO CODE

#PREVIOUS WEEK


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
"""

class ConfirmClient: #class to verify the identify of the client attempting to user ATM
    def __init__(self):
        # dictionary of client accounts and their personal identification number (pin)
        self.accounts = {
        101: {"pin": 1234,},
        102: {"pin": 2345,},
        103: {"pin": 3456, },
        }

    def check_account(self, kwargs): #method to confirm existance of the client
        self.__init__(self) #invoke account dictionary
        d_user = kwargs  #collect user provided data
        user_account = d_user["user_account"]  #extract data provided by user
        msg_account=""  #message of confirmation or error for transaction log
        msg_pin=""  #message of confirmation or error for transaction log
        flag_account = bool  #variable to store confirmation results
        flag_pin_ = bool   #variable to store result if account confirmed
        d_in_pin = {}  #placeholder for key:value pair to be provided to pin confirmation method
        d_pin = {}  #placeholder for results from check_pin method
        d_confirm = {}  #placholder for results of check_account method
        for keys, values in self.accounts.items(): #look into the account dictionary
            if keys == user_account: #if the account number is found
                flag_account = True  #results of account validation
                d_in_pin[keys] = values  #create key:value pair as input to check_pin method
                msg_account = "Account number confirmed."  #message for transaction log
        try: #check for undesired outcome
            if flag_account != True:
                raise TypeError
        except TypeError:   #handling of undesired outcome
            msg_account = "Invalid card account number provided."  #message for transaction log
            msg_pin = "Pin validation was not processed."  #message for transaction log
            flag_account = False  #results of account validation
            flag_pin = None  #pin set to None, validation dependent on account validation
            d_confirm["flag_account"] = flag_account  #append results of account validation
            d_confirm["msg_account"] = msg_account  #append message for transaction log
            d_confirm["flag_pin"] = flag_pin  #append results that pin was not validate as account was not validated
            d_confirm["msg_pin"] = msg_pin  #append message for transaction log

        else:  #handling of desired outcome
            d_pin = ConfirmClient.check_pin(self, d_user, d_in_pin)  #call check_pin method for  pin validation
            d_confirm["flag_account"] = flag_account  #append results of account validation
            d_confirm["msg_account"] = msg_account  #append message for transaction log
            d_confirm.update(d_pin)  #append results from check_in method
        return d_confirm #return confirmation flag

    def check_pin(self, d_user, kwargs):  #method to confirm the client personal identification number "pin"
        user_account = d_user["user_account"]  #extract data provided by user
        user_pin = d_user["user_pin"]  #extract data provider by user
        d_temp = kwargs
        flag_pin = bool  #variable to store result if account confirmed
        msg_temp="" #message of confirmation or error for transaction log
        d_temp_response = {}
        for keys, values in d_temp.items():  #look into account dictionary
            if keys == user_account:  #for the account provided
                for k, v in values.items():  #look into sub dictionary
                    if k == "pin": #if the pin
                        if v == user_pin: # if the value in dictionary is equal to value provided by the client
                            flag_pin = True  #results of personal identification number validation
                            msg_temp = "Pin confirmed."  #message for transaction log
        try:  #check for undesired outcome
            if flag_pin != True:
                raise TypeError
        except TypeError:  #handling of undesired outcome
            flag_pin = False  #results of personal identification number validation
            msg_temp = "Pin could not be confirmed."  #message for transaction log
        d_temp_response["flag_pin"]=flag_pin  #create key:value pair for method response
        d_temp_response["msg_pin"]=msg_temp   #create key:value pair for method response
        return d_temp_response #return confirmation of personal identification number

class ServiceSelection: #class to identify what type of transaction the client wanted to do.

    def transaction_type(self): #class method for identifying the type of transaction requested
        options = ["C", "D", "W", "T"] #collection of acceptable responses for control try
        tran_type = "" #temp variable for storing transaction type
        d_temp = {} #key:value pair for transaction choice
        print("Please select from the following options:\t") #greet client
        print('"C" for Check Balance of your accounts.') #check balance offering
        print('"D" for Deposit funds.') #deposit offering
        print('"W" for Withdrawal funds.') #withdrawal offering
        print('"T" for Transfer funds.') #transfer funds offering
        tran_type = input("Please make your selection.\t") #collect decision from user
        tran_type = tran_type.upper()
        d_temp["tran_type"]=tran_type  #key:value pair for transaction history and other methods
        print("You selected:\t", tran_type) #user alert
        try:  #check for undesired outcome
            if tran_type not in options:
                raise TypeError
        except TypeError:  #action for undesired outcome
            print("Invalid transaction selected.")
            print("Please visit the teller for assistance")
            exit()
        else: #action for desired outcome
            return d_temp

class Transactions: #class for all transaction types supported
    #class level dictionary of account details

    def __init__(self):

        self.account_details = {
            101: {"checking": 501,
                  501: 4500.0,
                  "saving": 601,
                  601: 5000.0,
                  "name": "Erin Church",
                  },
            102: {"checking": 502,
                  502: 3500.0,
                  "saving": 602,
                  602: 12000.0,
                  "name": "Ronald Williams",
                  },
            103: {"checking": 503,
                  503: 1200.0,
                  "saving": 603,
                  603: 2300.0,
                  "name": "Dirk Church",
                  },
        }
        #class level dictionary of all transaction history
        self.tran_history = {
            1: {"tran_type": "check_balance",
                "account": 101,
                "sub_account_type": "checking",
                "sub_account": 501,
                "sub_account_balance": 4500.0,
                "sub_account_type": "savings",
                "sub_account": 601,
                "sub_account_balance": 3500.0,
                "tran_amount": 0,
                },
            2: {"tran_type": "check_balance",
                "account": 102,
                "sub_account_type": "checking",
                "sub_account": 502,
                "sub_account_balance": 3500.0,
                "sub_account_type": "savings",
                "sub_account": 601,
                "sub_account_balance": 12000.0,
                "tran_amount": 0,
                },
            3: {"tran_type": "check_balance",
                "account": 103,
                "sub_account_type": "checking",
                "sub_account": 503,
                "sub_account_balance": 1200.0,
                "sub_account_type": "savings",
                "sub_account": 603,
                "sub_account_balance": 2300.0,
                "tran_amount": 0,
                }
        }


    def Transaction_Calls(self, tran, c):
#        self.account_details
#        self.tran_history
        if tran == "D": #should add additional logic to help prevent failures and illogical values
            t = Transactions.deposit_funds(self, c) #call transaction method for depositing funds into an account
            print("Your deposit and new account balance:\t", t) #confirm transactiont to user
        elif tran == "C": #should add additional logic to help prevent failures and illogical values
            t = Transactions.check_balance(self, c) #call transaction method to check balances
            print("Current status of your accounts:\t") #print client alert message
            print(t[0]) #returns the account numbers and balance of their first account
            print(t[1]) #returns the account numbers and balance of their second account
        elif tran == "W": #should add additional logic to help prevent failures and illogical values
            s = Transactions.check_funds(self,c) #method call, confirm client has sufficient funds
#            print(s) #developer check
            t = Transactions.withdraw_funds(self,c, s[0], s[1], s[2], s[3]) #method call to complete the withdrawal
            print("Your withdrawal and new account balance:\t",t) #alert to user of their transaction
        elif tran == "T": #should add additional logic to help prevent failures and illogical values
            s = Transactions.check_funds(self,c) #method call to confirm client has sufficient funds
            print("results, check funds.\t", s) #developer test
            u = Transactions.transfer_account(self, c, s[3]) #method call to confirm destination account
            print("results, transfer account validation.\t", u) #developer test
            t = Transactions.withdraw_funds(self, c, s[0], s[1], s[2], s[3]) #method call to withdrawl funds from client account
            print("Your withdrawal and new account balance:\t", t) #alert to user of withdrawn funds for transfer
            v = Transactions.transfer_deposit(self, c, s[0], u[0], u[1], u[2], u[3]) #method call to deposit transfer amount in destination account
            print("Your transferred amount and the destination account:\t", v[0], v[1]) #alert to user of transfered funds and the destiation


    def check_funds(self,c):
        self.__init__(self)
#        self.account_details #initiate access to client dictionary
#        self.tran_history #initiate access to transaction history dictionary
        tran_amount = float(input("Please enter the amount you with to withdraw.\t")) #ask user for transaction amount
        sub_acct_type = input("Withdraw from checking or savings account? (Type checking or saving)") #ask what type of account they want to transact from
        sub_acct = 0 #temp variable to fetch sub account number
        sub_acct_bal = 0 #temp variable for storing the sub accounts balances
        flag_sufficient_funds = bool #flag to determine if the client has enough money to make desired transaction
        for keys, values in self.account_details.items(): #look in client account dictinoary
            if keys == c: #if the account number matches that of the client's account number
                for k, v in values.items(): #look in the sub-dictionaries
                    if k == sub_acct_type: #if the sub account type matches what was provided by the user
                        sub_acct = v #store the sub account number
                    elif k == sub_acct: #now that you have the sub account number, match to its key
                        sub_acct_bal = v #store the balance of the sub account
                        if sub_acct_bal >= tran_amount: #verify if there is more money, or equal money, to the clients desired transaction
                            flag_sufficient_funds = True #if there is, then set the flag equal to True
                        else:
                            print("Insufficient funds.\t") #if not, then set flag to False and tell the user
                            flag_sufficient_funds = False #set flag to false
#        print(sub_acct_type, sub_acct, flag_sufficient_funds) #developer test
        return tran_amount, sub_acct_type, sub_acct, flag_sufficient_funds  #return variable

    def withdraw_funds(self,c, tran_amount, sub_account_type, sub_account, flag_sufficient_funds):  #method to actually take funds from client account
        self.__init__(self)

#        self.account_details #invoke client account details
#        self.tran_history #invoke transaction history
        d_sub_temp = {"tran_type":"withdrawal",} #seed values for transaction log
        d_sub_temp["account"] = c #set account for transaction log
        d_sub_temp["sub_account_type"]=sub_account_type #set sub account type for tranaction log
        sub_acct_bal = 0 #variable to capture temporary starting balance of account
        temp_bal = 0 #variable to capture temporary calculated ending balance of account
        if flag_sufficient_funds == True: #only process if there is sufficient funds for the client to continue
            for keys, values in self.account_details.items(): #look into account details
                if keys == c: #if the account matches that of the clients
                    for k, v in values.items(): #look into the sub dictionaries
                        if k == sub_account: #if the account matches the earlier identified sub account
                            sub_acct_bal = v #store the begining balance of the account
                            d_sub_temp["sub_account_balance_begin"] = v #update the transaction history for begining balance
                            temp_bal = v - tran_amount #calculate the balance after the transaction
                            self.account_details[c][k] = temp_bal #update the client account dictionary with new post transaction balance
                            d_sub_temp["transaction_amount"] = tran_amount #update transaction history with transaction amount
                            d_sub_temp["sub_account_balance_end"] = temp_bal #update transaction history with the post transaction ending balance
#                            print(self.account_details[c][k]) #developer check
        self.tran_history[6] = d_sub_temp #append transaction history to main transaction history dictionrary
        print("Transaction executed:\t", self.tran_history[6]) #alert to system or user
        final_balance = self.account_details[c][sub_account]
        return tran_amount, final_balance

    def transfer_account(self,c, flag_sufficient_funds): #method to verify if destination account provided by user for their transfer
        self.account_details #invoke account details
        to_account = 0 #temp variable for the destination account
        to_sub_account_type = "" #temp variable for the destination account type
        to_sub_account = 0 #temp variable for destination sub account
        flag_transfer_account_valid = bool #flag to confirm if destination account is valid
        if flag_sufficient_funds == True: #check the client had sufficient funds, if not, don't bother
            to_account = int(input("Please provide the account number to receive your transfer.\t")) #get the destination account from the user
            to_sub_account_type = input("Is it a checkings or savings account? Type checking or saving.\t") #get the destination account type from the user
            for keys, values in self.account_details.items(): #look into client account details
                if keys == to_account: #if account matches client provided destination account
                    for k, v, in values.items(): #look into the sub dictionary of accounts
                        if k == to_sub_account_type: #if it matches the account type
                            to_sub_account = v #store the sub account number
#                            print(to_sub_account) #developer check
                            flag_transfer_account_valid = True #confirm the destination account is valid
#                            print(flag_transfer_account_valid) #developer check
#                            print(to_account, to_sub_account_type, to_sub_account, flag_transfer_account_valid) #developer check
        return to_account, to_sub_account_type, to_sub_account, flag_transfer_account_valid #return information collected and derived

    def transfer_deposit(self, c, tran_amount, to_account, to_sub_account_type, to_sub_account, flag_transfer_account_valid): #method to deposit the transfered amount to the desintation account
        self.__init__(self)

#        self.account_details #invoke account details
#        self.tran_history #invoke transaction details
        d_sub_temp = {"tran_type":"transfer deposit",} #seed transaction history temp dictionary
        d_sub_temp["account"] = to_account #update transaction history temp with client specified destination account
        d_sub_temp["sub_account_type"] = to_sub_account #update transaction history temp with destination sub account derived
        d_sub_temp["from_account"] = c #update transaction history temp with original clients account
        d_sub_temp["sub_account_type"]= to_sub_account_type  #update transaction history temp with destination account type specified by user
        d_sub_temp["transaction_amount"] = tran_amount #update transaction history temp with the transaction transfer amount specified by client
        sub_acct_bal = 0 #temp variable for collecting begining account balance of destination account
        temp_bal = 0 #temp variable for calculated balance after transfer deposit

        if flag_transfer_account_valid == True: #only execute if client provided a valid destination account
            for keys, values in self.account_details.items(): #look into account dictionary
                if keys == to_sub_account: #if account equals the destination account specified by client
                    for k, v in values.items(): #look into sub dictionaries
                        if k == to_sub_account: #if sub account equals the sub account derived
                            sub_acct_bal = v #store the begining balance
                            d_sub_temp["to_account_balance_begin"] = v #update transaction history temp with beginning balance
                            temp_bal = v + tran_amount #calculate what balance should be after the deposit is made
                            d_sub_temp["to_account_balance_end"] = temp_bal #update transaction history temp with new balance
                            self.account_details[to_account][to_sub_account] = temp_bal #update client account dictionary with new balance
#                            print(self.account_details[k][v]) #developer check
        final_balance = self.account_details[to_account][to_sub_account] #set final balance, but not returned to protect other clients privacy
        self.tran_history[8]=d_sub_temp #update transaction history to include temp history content
        print("Transaction executed:\t",self.tran_history[8]) #developer check
        return tran_amount, to_account #return used data

    def deposit_funds(self, c): #method for depositing funds, without a transfer
        self.__init__(self)
#        self.account_details #invoke account details
#        self.tran_history #invoke transaction history
        tran_amount = float(input("Please enter the amount you wish to deposit.")) #collect deposit amount
        sub_acct_type = input("Deposit to checkings or savings account? (Type checking or saving)\t") #collect the type of account they wanted to deposit the funds to
        sub_acct = 0 #placeholder for the sub account
        sub_acct_bal = 0 #placeholder for the starting balance fo the sub account
        temp_bal = 0 #placeholder for the calculate balance after the deposit
        final_balance = 0
        d_sub_temp = {"tran_type":"deposit",} #see transaction history temp with deposit transaction
        d_sub_temp["account"] = c #add account to transaction history temp
        d_sub_temp["sub_account_type"]=sub_acct_type #add sub account type to transaction history temp
        for keys, values in self.account_details.items(): #look into account details dictionary
            if keys == c: #if the account equals that provided by the client
                for k, v in values.items(): #look into the sub dictionaries
                    if k == sub_acct_type: #if the account type matches the type provided by client
                        sub_acct = v #store the sub account number
                        d_sub_temp["sub_account"] = sub_acct #provide sub account number to transaction history temp
                    elif k == sub_acct: #now you have the sub account number, look at its contents
                        sub_acct_bal = v #collect the begining balance of the sub account
                        temp_bal = v + tran_amount #calculate the new balance, with clients deposit
                        d_sub_temp["sub_account_balance_begin"] = sub_acct_bal #update transaction history temp with ending balance
                        self.account_details[c][k] = temp_bal #update actual sub account balance
                        final_balance = self.account_details[c][k] #collect final balance
                        d_sub_temp["transaction_amount"] = tran_amount #update transaction amount in transaction history temp
                        d_sub_temp["sub_account_balance_end"] = temp_bal #update ending sub account balance in transaction history temp
#                        print(self.account_details[c][k]) #developer check
        self.tran_history[5] = d_sub_temp #update transaction history with the contents of the temp dictionary
        print("Transaction executed:\t",self.tran_history[5]) #developer check
        return tran_amount, final_balance #return balances

    def check_balance(self, c): #method for allowing client ot check their balances
        self.__init__(self)

#        self.tran_history #invoke transaction history
#        self.account_details #invoke account details
        sub_acct_1 = 0 #temp variable for sub account number
        sub_acct_2 = 0 #temp variable for sub account number
        sub_type_1 = "" #temp variable for sub account type
        sub_type_2 = "" #temp vriable for sub account type
        d_account_1 = {} #temp dictionary for sub accounts details
        d_account_2 = {} #temporary dictionary for sub account details
        d_sub_temp = {"tran_type": "check_balance", #see transaction history temp for check balances
                      "account": c, }
        d_account_1["account"] = c #update parent account for temp dictionary
        d_account_2["account"] = c #update parent account for temp dictionary
        for keys, values in self.account_details.items(): #look into account details
            if keys == c: #if account matches that provided by client
                for k, v in values.items(): #look into sub account dictionaries
                    if k == "checking": #if the account has a checking account
                        sub_type_1 = "checking" #set the temp type to checking
                        sub_acct_1 = v #collect the sub account number for the checking account
                        d_sub_temp[sub_type_1] = sub_acct_1 #update sub account number to transaction history
                        d_account_1["type"] = sub_type_1 #update temp dictionary with checking type
                        d_account_1["checking account"] = sub_acct_1 #update temp dictionary with checking balance
#                        print(k, v) #developer check
                    elif k == "savings": #if there is a savings account
                        sub_type_2 = "savings"  #set temporary type to savings
                        sub_acct_2 = v #capture the sub account number for savings account
                        d_sub_temp[sub_type_2] = sub_acct_2 #populate transaction history temp
                        d_account_2["type"] = sub_type_2 #update temp dictionary for type
                        d_account_2["saving account"] = sub_acct_2 #update the account number for temp dictionary
#                        print(k, v) #developer check
                    elif k == sub_acct_1: #now that you have the sub account number, first account
                        d_sub_temp[sub_acct_1] = v #collect the balance for transction history temp
                        d_account_1["balance"] = v #collect the balance for the temporary dictinary
#                        print(k, v) #developer check
                    elif k == sub_acct_2: #now that you have the sub account, second account
                        d_sub_temp[sub_acct_2] = v #collect balance for the transaction history temp
                        d_account_2["balance"] = v #collect balance for dictionary temp
#                        print(k, v) #developer check
        self.tran_history[4] = d_sub_temp #update transction history
        print("Transaction executed:\t",self.tran_history[4]) #print transaction history
        return d_account_1, d_account_2 #return temporary dictionaries for client notification

class Bank:
    pass

class ClientATM:
    b = ConfirmClient  # invoke class for confirming the client identity
    c = int(input("Please provide your card number.\t"))  # collect client card/account number
    p = int(input("Please enter your pin number.\t"))  # collect client pin number
    d_user = {}  # placeholder to store user input
    d_user["user_account"] = c  # key:value pair for user input of account/card number
    d_user["user_pin"] = p  # key:value pair for user input of personal identification number
    confirmation = {}  # placeholder of check_account and check_pin method results
    confirmation = ConfirmClient.check_account(b, d_user)  # call class method and set temp variable for confirming client account identify
    flag_account = confirmation["flag_account"] #retrieve confirmation flag for account number
    flag_pin = confirmation["flag_pin"]  #retreive confirmaiton flag for pin number

    try: #evaluate undesired outcome
        if flag_account != True or flag_pin != True:
            raise TypeError
    except TypeError:  #action for undesired outcome
        print(confirmation["msg_account"])
        print(confirmation["msg_pin"])
        print("Apologies but we cannot complete your desired transactions.")
        print("Please visit the Teller.")
        exit()
    else:   #action for desired outcome
        e = ServiceSelection  # invoke class for making client transaction selection
        d_tran = ServiceSelection.transaction_type(e)  # call class method and setting temporary variable for selection made
        print("client ATM", tran)
        f = Transactions
        Transactions.Transaction_Calls(f, d_user, d_tran)


class Teller:
    pass


def main():
    ClientATM()

"""    
    try:
        flags = ConfirmClient.check_account(a, d_user) #call class method and set temp variable for confirming client account identify
    except:
        pass
#        flags == TypeError
#        print("Please start over.\t")
#        print("Apologies, we cannot confirm your account.\n") #rejection message
#        print("Please see a teller.\t") #instruction message
    else:
        pass
"""

"""
    if flag_account == True and flag_pin == True: #only execute if the client identity is confirmed
        print("Account confirmed.\t") #notice to client
        b = ServiceSelection  # invoke class for making client transaction selection
        tran = ServiceSelection.transaction_type(b)  # call class method and setting temporary variable for selection made
        d = Transactions  # invoke class for transactions
        e = Transactions.Transaction_Calls(d, tran, c)  # calling class methods and setting temporary variable for executing client transactions
    else:
        print("Apologies, we cannot confirm your account.\n") #rejection message
        print("Please see a teller.\t") #instruction message
"""
if __name__ == "__main__":
    main() #call main function