#THIS WEEK

# from previous week keep basic functionality of atm

#add try/catch for errors

#consider trying to figure out how init works

#create 3 classes for profiles, the bank, the teller, and the customer via atm

#what is in main at the moment is the customer via atm

#the teller would only need to confirm accounts, not pin numbers, maybe they see the before and after balances for transfers

#the bank is very similar to the teller maybe just the input is different?

#look into the #args and the #kwargs? didn't figure out how to use those

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


class ConfirmClient: #class to verify the identify of the client attempting to user ATM
    #dictionary of client accounts and their personal identification number (pin)
    """ accounts = {
        101: {"pin": 1234,},
        102: {"pin": 2345,},
        103: {"pin": 3456, },
    } """
    def __init__(self):

        self.accounts = {
        101: {"pin": 1234,},
        102: {"pin": 2345,},
        103: {"pin": 3456, },
        }

    def check_account(self, c): #method to confirm existance of the client
        self.__init__(self) #invoke account dictionary
#        self.accounts #invoke account dictionary
        flag_account_confirm = bool #variable to store confirmation results
        for keys, values in self.accounts.items(): #look into the account dictionary
            if keys == c: #if the account number is found
                flag_account_confirm = True #then the account number is confirmed
#                print(flag_account_confirm) #developer check
#        print("checking confirm account class level dictionary.\t", self.accounts.items()) #developer check
        return flag_account_confirm #return confirmation flag

    def check_pin(self, c, p): #method to confirm the client personal identification number "pin"
        self.__init__(self) #invoke account dictionary
#        self.accounts #invoke account dictionary
        flag_pin_confirm = bool  #variable to store result if account confirmed
        for keys, values in self.accounts.items(): #look into account dictionary
            if keys == c: #for the account provided
                for k, v in values.items(): #look into sub dictionary
                    if k == "pin": #if the pin
                        if v == p: # if the value in dictionary is equal to value provided by teh client
                            flag_pin_confirm = True #then set the flag to True
#                            print(flag_pin_confirm) #developer check
#        print("checking confirm pin class level dictionary.\t", self.accounts.items()) #developer check
        return flag_pin_confirm #return confirmation of personal identification number

class ServiceSelection: #class to identify what type of transaction the client wanted to do.

    def transaction_type(self): #class method for identifying the type of transaction requested
        tran_type = "" #temp variable for storing transaction type
        print("Please select from the following options:\t") #greet client
        print('"C" for Check Balance of your accounts.') #check balance offering
        print('"D" for Deposit funds.') #deposit offering
        print('"W" for Withdrawal funds.') #withdrawal offering
        print('"T" for Transfer funds.') #transfer funds offering
        tran_type = input("Please make your selection.\t") #collect decision from user
        print("You selected:\t", tran_type) #user alert
        #to do: build controls for values provided
        return tran_type #give back to program the client selection

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
    pass


class Teller:
    pass


def main():
    a = ConfirmClient #invoke class for confirming the client identity
    c = int(input("Please provide your card number.\t")) #collect client card/account number
    flag_account = ConfirmClient.check_account(a, c) #call class method and set temp variable for confirming client account identify
    p = int(input("Please enter your pin number.\t")) #collect client pin number
    flag_pin = ConfirmClient.check_pin(a, c, p) #call class method and set temp variable for confirming personal identification number

    if flag_account == True and flag_pin == True: #only execute if the client identity is confirmed
        print("Account confirmed.\t") #notice to client
        b = ServiceSelection  # invoke class for making client transaction selection
        tran = ServiceSelection.transaction_type(b)  # call class method and setting temporary variable for selection made
        d = Transactions  # invoke class for transactions
        e = Transactions.Transaction_Calls(d, tran, c)  # calling class methods and setting temporary variable for executing client transactions
    else:
        print("Apologies, we cannot confirm your account.\n") #rejection message
        print("Please see a teller.\t") #instruction message

if __name__ == "__main__":
    main() #call main function