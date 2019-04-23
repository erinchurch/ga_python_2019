

"""
PSEUDO CODE
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


class ATMConfirmClient: #class to verify the identify of the client attempting to user ATM
    def __init__(self):
        # dictionary of client accounts and their personal identification number (pin)
        self.accounts = {
        101: {"pin": 1234,},
        102: {"pin": 2345,},
        103: {"pin": 3456, },
        }

    def atm_check_account(self, kwargs): #method to confirm existance of the client
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
            d_pin = ATMConfirmClient.atm_check_pin(self, d_user, d_in_pin)  #call check_pin method for  pin validation
            d_confirm["flag_account"] = flag_account  #append results of account validation
            d_confirm["msg_account"] = msg_account  #append message for transaction log
            d_confirm.update(d_pin)  #append results from check_in method
        return d_confirm #return confirmation flag

    def atm_check_pin(self, d_user, kwargs):  #method to confirm the client personal identification number "pin"
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


class ConfirmBankTeller: #class to verify the identify of the client attempting to user ATM
    def __init__(self):
        # dictionary of client accounts and their personal identification number (pin)
        self.users = {
            "teller1": {"password": "teller1",},
            "bank1": {"password": "bank1",},
        }
        self.account_details = {
            101: {"checking": 501,
                  501: 4500.0,
                  "saving": 601,
                  601: 5000.0,
                  "name": "Erin Church",
                  "username": "erinchurch",
                  "card_checking": 101,
                  "card_saving":101,
                  "pin": 1234,
                  },
            102: {"checking": 502,
                  502: 3500.0,
                  "saving": 602,
                  602: 12000.0,
                  "name": "Ronald Williams",
                  "username": "ronaldwilliams",
                  "card_checking": 102,
                  "card_saving":102,
                  "pin": 2345,
                  },
            103: {"checking": 503,
                  503: 1200.0,
                  "saving": 603,
                  603: 2300.0,
                  "name": "Dirk Church",
                  "username": "dirkchurch",
                  "card_checking": 103,
                  "card_saving":103,
                  "pin":3456
                  },
        }


    def check_user(self, kwargs): #method to confirm existance of the client
        self.__init__(self) #invoke account dictionary

        #local variables
        d_temp = {}
        msg_user = ""
        msg_password = ""
        flag_user = bool
        flag_password = bool
        d_in_password = {}
        d_pwd = {}

        try:
            d_user = kwargs  # collect user provided data
            user_account = d_user["username"]  # extract data provided by user

        except KeyError:
            msg_user = "Issue experienced with log in data, user not validated"
            flag_user = None
            msg_password = "Issue experienced with log in data, password not validated"
            flag_password = None
            d_temp["check_user_message"] = msg_user
            d_temp["flag_user"] = flag_user
            d_temp["check_password_message"] = msg_password
            d_temp["flag_password"] = flag_password

            return d_temp
        else:
            for keys, values in self.users.items(): #look in user dictionary
                if keys == user_account:
                    d_in_password[keys] = values
                    msg_user = "User name confirmed."
                    flag_user = True
                    d_temp["check_user_message"] = msg_user
                    d_temp["flag_user"] = flag_user

            try:
                if flag_user != True:
                    raise TypeError

            except TypeError:

                msg_user = "User name could not confirmed."
                flag_user = False
                msg_password = "User name not confirmed, password not validated"
                flag_password = False
                d_temp["check_user_message"] = msg_user
                d_temp["flag_user"] = flag_user
                d_temp["check_password_message"] = msg_password
                d_temp["flag_password"] = flag_password
                return d_temp

            else:

                if flag_user == True:
                    d_pwd = ConfirmBankTeller.check_password(self, d_user, d_in_password)
                    d_temp.update(d_pwd)
                    return d_temp


    def check_password(self, kwargs_1, kwargs_2):
        #local variables
        msg = ""
        flag_password = bool
        d_temp = {}
        try: #check method input variables
            d_user = kwargs_1  # collect user provided data
            user_account = d_user["username"]  # extract data provided by user
            user_pwd = d_user["password"]  # extract data provided by user
            d_password_confirm = kwargs_2
        except KeyError:  #method action for incomplete or invalid input
            msg_password = "Issue experienced with log in data, password not validated"
            flag_password = None
            d_temp["check_password_message"] = msg_password
            d_temp["flag_password"] = flag_password
            return d_temp

        else:
            for keys, values in d_password_confirm.items():
                if keys == user_pwd:
                    for k, v in values.items():
                        if v == user_pwd:
                            msg_password = "User password validated"
                            flag_password = True
                            d_temp["check_password_message"] = msg_password
                            d_temp["flag_password"] = flag_password
                            return d_temp
            try:
                if flag_password != True:
                    raise TypeError

            except TypeError:
                msg_password = "User password could not be validated."
                flag_password = False
                d_temp["check_password_message"] = msg_password
                d_temp["flag_password"] = flag_password
                return d_temp

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


    def __init__(self):

        self.account_details = {
            101: {"checking": 501,
                  501: 4500.0,
                  "saving": 601,
                  601: 5000.0,
                  "name": "Erin Church",
                  "username":"erinchurch",
                  "account_card":101,
                  },
            102: {"checking": 502,
                  502: 3500.0,
                  "saving": 602,
                  602: 12000.0,
                  "name": "Ronald Williams",
                  "username": "ronaldwilliams",
                  "account_card": 102,
                  },
            103: {"checking": 503,
                  503: 1200.0,
                  "saving": 603,
                  603: 2300.0,
                  "name": "Dirk Church",
                  "username": "dirkchurch",
                  "account_card": 103,
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


    def teller_transaction_calls(self, user, tran):
        account = user["client_account"]
        tran = tran["tran_type"]
        if tran == "D": #should add additional logic to help prevent failures and illogical values
            t = Transactions.deposit_funds(self, account) #call transaction method for depositing funds into an account
            self.tran_history[5.1] = user
            self.tran_history[5.2] = tran
            self.tran_history[5.3] = t
            print(self.tran_history.items())
            t_msg = t["deposit_message"]
            try:
                t_1 = t["sub_account_balance_begin"]
                t_2 = t["transaction_amount"]
                t_3 = t["sub_account_balance_end"]
            except KeyError:
                print("Transaction issue, please escalate.")
                #insert a system alert to notify the Bank to investigate any issues
            else:
                print("The account balance before deposit:\t", t_1) #confirm transactiont to user
                print("The deposit amount:\t", t_2) #confirm transactiont to user
                print("The account balance after deposit:\t", t_3) #confirm transactiont to user
        elif tran == "C": #should add additional logic to help prevent failures and illogical values
            t = Transactions.check_balance(self, account) #call transaction method to check balances
            self.tran_history[3.1] = user  #append transaction history to main transaction history dictionrary
            self.tran_history[3.2] = tran  #append transaction history to main transaction history dictionrary
            self.tran_history[3.3] = t  #update transaction history with contents of checking account balances
            print(self.tran_history.items())

            try:
                t_msg1 = t["check_balance_message"]
                t_msg2 = t["checking_balance_message"]
                t_msg3 = t["saving_balance_message"]
                t_bal1 = t["checking_balance_amount"]
                t_bal2 = t["saving_balance_amount"]

                print(t_msg1)
                print(t_msg2)
                print(t_msg3)
                print("Available Funds in Checking:\t", t_bal1)
                print("Available Funds in Savings:\t", t_bal2)

            except KeyError:

                try:
                    t_msg1 = t["check_balance_message"]
                    t_msg2 = t["checking_balance_message"]
                    t_bal1 = t["checking_balance_amount"]
                    print(t_msg1)
                    print(t_msg2)
                    print("Available Funds in Checking:\t", t_bal1)

                except KeyError:

                    try:
                        t_msg1 = t["check_balance_message"]
                        t_msg3 = t["saving_balance_message"]
                        t_bal2 = t["saving_balance_amount"]
                        print(t_msg1)
                        print(t_msg3)
                        print("Available Funds in Savings:\t", t_bal2)

                    except KeyError:
                        print("Technical issues accessing account information, please escalate.")
        elif tran == "W": #should add additional logic to help prevent failures and illogical values
            s = Transactions.check_funds(self, account) #method call, confirm client has sufficient funds
            t = Transactions.withdraw_funds(self, account, s)  # method call to complete the withdrawal
            self.tran_history[6] = user  # append transaction history to main transaction history dictionary
            self.tran_history[6.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[6.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[6.3]= t # append transaction history to main transaction history dictionary
            try:
                s_msg = s["check_funds_message"]
                s_tran = s["tran_amount"]
                t_msg = t["withdrawal_message"]
                t_beg = t["withdrawal_begin_balance"]
                t_end = t["withdrawal_end_balance"]
            except KeyError:
                print("Issue with transaction, please escalate.")
                #insert a system alert for the bank to investigate any issues with the application
            else:
                print(s_msg) #user notification
                print("Withdrawal amount requested:\t", s_tran) #user notification
                print(t_msg) #user notification
                print("Initial account balance:\t", t_beg) #user notification
                print("Ending account balance:\t", t_end) #user notification
                print(self.tran_history.items()) #developer check
        elif tran == "T": #should add additional logic to help prevent failures and illogical values

            s = Transactions.check_funds(self, account) #method call to confirm client has sufficient fund
            u = Transactions.transfer_account(self, s) #method call to confirm destination account
            t = Transactions.transfer_withdraw(self, account, s, u) #method call to withdrawl funds from client account
            v = Transactions.transfer_deposit(self, s, u) #method call to deposit transfer amount in destination account
            self.tran_history[8] = user  # append transaction history to main transaction history dictionary
            self.tran_history[8.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[8.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[8.3]= u # append transaction history to main transaction history dictionary
            self.tran_history[8.4] = t  # append transaction history to main transaction history dictionary
            self.tran_history[8.5] = v  # append transaction history to main transaction history dictionary

            try:
                s_msg = s["check_funds_message"]
                s_tran = s["tran_amount"]
                u_msg = u["transfer_account_message"]
                t_msg = t["transfer_withdraw_message"]
                t_beg = t["transfer_withdraw_begin_balance"]
                t_end = t["transfer_withdraw_end_balance"]
                v_msg = v["transfer_deposit_message"]
                v_beg = v["transfer_deposit_begin_balance"]
                v_end = v["transfer_deposit_end_balance"]
                print(s_msg) #user notification
                print("Transfer amount requested:\t", s_tran) #user notification
                print(u_msg) #user notification
                print(t_msg) #user notification
                print("Initial client account balance:\t", t_beg) #user notification
                print("Ending client account balance:\t", t_end) #user notification
                print(v_msg) #user notification
                print("Initial transfer account balance:\t", t_beg)  # user notification
                print("Ending transfer account balance:\t", t_end)  # user notification


            except KeyError:
                s_msg = s["check_funds_message"]
                s_tran = s["tran_amount"]
                u_msg = u["transfer_account_message"]
                t_msg = t["transfer_withdraw_message"]
                v_msg = v["transfer_deposit_message"]
                print(s_msg) #user notification
                print("Transfer amount requested:\t", s_tran) #user notification
                print(u_msg) #user notification
                print(t_msg)  # user notification
                print(v_msg)  # user notification

            else:
                print("Issue with transaction, please escalate")
                #insert a system alert for the bank to investigate any issues with the application


    def bank_transaction_calls(self, user, tran):
        account = user["client_account"]
        tran = tran["tran_type"]
        if tran == "D": #should add additional logic to help prevent failures and illogical values
            t = Transactions.deposit_funds(self, account) #call transaction method for depositing funds into an account
            self.tran_history[5.1] = user
            self.tran_history[5.2] = tran
            self.tran_history[5.3] = t
            print(self.tran_history.items())
        elif tran == "C": #should add additional logic to help prevent failures and illogical values
            t = Transactions.check_balance(self, account) #call transaction method to check balances
            self.tran_history[3.1] = user  #append transaction history to main transaction history dictionrary
            self.tran_history[3.2] = tran  #append transaction history to main transaction history dictionrary
            self.tran_history[3.3] = t  #update transaction history with contents of checking account balances
            print(self.tran_history.items())
        elif tran == "W": #should add additional logic to help prevent failures and illogical values
            s = Transactions.check_funds(self, account) #method call, confirm client has sufficient funds
            t = Transactions.withdraw_funds(self, account, s)  # method call to complete the withdrawal
            self.tran_history[6] = user  # append transaction history to main transaction history dictionary
            self.tran_history[6.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[6.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[6.3]= t # append transaction history to main transaction history dictionary
            print(self.tran_history.items()) #developer check
        elif tran == "T": #should add additional logic to help prevent failures and illogical values

            s = Transactions.check_funds(self, account) #method call to confirm client has sufficient fund
            u = Transactions.transfer_account(self, s) #method call to confirm destination account
            t = Transactions.transfer_withdraw(self, account, s, u) #method call to withdrawl funds from client account
            v = Transactions.transfer_deposit(self, s, u) #method call to deposit transfer amount in destination account
            self.tran_history[8] = user  # append transaction history to main transaction history dictionary
            self.tran_history[8.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[8.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[8.3]= u # append transaction history to main transaction history dictionary
            self.tran_history[8.4] = t  # append transaction history to main transaction history dictionary
            self.tran_history[8.5] = v  # append transaction history to main transaction history dictionary
            print(self.tran_history.items())


    def atm_transaction_calls(self, user, tran):
        account = user["user_account"]
        tran = tran["tran_type"]
        if tran == "D": #should add additional logic to help prevent failures and illogical values
            t = Transactions.deposit_funds(self, account) #call transaction method for depositing funds into an account
            self.tran_history[5.1] = user
            self.tran_history[5.2] = tran
            self.tran_history[5.3] = t
            print(self.tran_history.items())
            t_msg = t["deposit_message"]
            print(t_msg)  # confirm transaction to user
            try:
                t_1 = t["sub_account_balance_begin"]
                t_2 = t["transaction_amount"]
                t_3 = t["sub_account_balance_end"]
            except KeyError:
                print("Please try your transaction again or see a Teller for assistance.")
                #insert a system alert to notify the Bank to investigate any issues
            else:
                print("Your account balance before your deposit:\t", t_1) #confirm transactiont to user
                print("Your deposit amount:\t", t_2) #confirm transactiont to user
                print("Your account balance after your deposit:\t", t_3) #confirm transactiont to user
        elif tran == "C": #should add additional logic to help prevent failures and illogical values
            t = Transactions.check_balance(self, account) #call transaction method to check balances
            self.tran_history[3.1] = user  #append transaction history to main transaction history dictionrary
            self.tran_history[3.2] = tran  #append transaction history to main transaction history dictionrary
            self.tran_history[3.3] = t  #update transaction history with contents of checking account balances
            print(self.tran_history.items())

            try:
                t_msg1 = t["check_balance_message"]
                t_msg2 = t["checking_balance_message"]
                t_msg3 = t["saving_balance_message"]
                t_bal1 = t["checking_balance_amount"]
                t_bal2 = t["saving_balance_amount"]

                print(t_msg1)
                print(t_msg2)
                print(t_msg3)
                print("Available Funds in Checking:\t", t_bal1)
                print("Available Funds in Savings:\t", t_bal2)

            except KeyError:

                try:
                    t_msg1 = t["check_balance_message"]
                    t_msg2 = t["checking_balance_message"]
                    t_bal1 = t["checking_balance_amount"]
                    print(t_msg1)
                    print(t_msg2)
                    print("Available Funds in Checking:\t", t_bal1)

                except KeyError:

                    try:
                        t_msg1 = t["check_balance_message"]
                        t_msg3 = t["saving_balance_message"]
                        t_bal2 = t["saving_balance_amount"]
                        print(t_msg1)
                        print(t_msg3)
                        print("Available Funds in Savings:\t", t_bal2)

                    except KeyError:
                        print("Technical issues with accessing your account information, please see teller.")
        elif tran == "W": #should add additional logic to help prevent failures and illogical values
            s = Transactions.check_funds(self, account) #method call, confirm client has sufficient funds
            t = Transactions.withdraw_funds(self, account, s)  # method call to complete the withdrawal
            self.tran_history[6] = user  # append transaction history to main transaction history dictionary
            self.tran_history[6.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[6.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[6.3]= t # append transaction history to main transaction history dictionary
            try:
                s_msg = s["check_funds_message"]
                s_tran = s["tran_amount"]
                t_msg = t["withdrawal_message"]
                t_beg = t["withdrawal_begin_balance"]
                t_end = t["withdrawal_end_balance"]
            except KeyError:
                print("Please try your transaction again or see a teller for assistance")
                #insert a system alert for the bank to investigate any issues with the application
            else:
                print(s_msg) #user notification
                print("Withdrawal amount requested:\t", s_tran) #user notification
                print(t_msg) #user notification
                print("Initial account balance:\t", t_beg) #user notification
                print("Ending account balance:\t", t_end) #user notification
                print(self.tran_history.items()) #developer check
        elif tran == "T": #should add additional logic to help prevent failures and illogical values

            s = Transactions.check_funds(self, account) #method call to confirm client has sufficient fund
            u = Transactions.transfer_account(self, s) #method call to confirm destination account
            t = Transactions.transfer_withdraw(self, account, s, u) #method call to withdrawl funds from client account
            v = Transactions.transfer_deposit(self, s, u) #method call to deposit transfer amount in destination account
            self.tran_history[8] = user  # append transaction history to main transaction history dictionary
            self.tran_history[8.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[8.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[8.3]= u # append transaction history to main transaction history dictionary
            self.tran_history[8.4] = t  # append transaction history to main transaction history dictionary
            self.tran_history[8.5] = v  # append transaction history to main transaction history dictionary

            try:
                s_msg = s["check_funds_message"]
                s_tran = s["tran_amount"]
                u_msg = u["transfer_account_message"]
                t_msg = t["transfer_withdraw_message"]
                t_beg = t["transfer_withdraw_begin_balance"]
                t_end = t["transfer_withdraw_end_balance"]
                v_msg = v["transfer_deposit_message"]
                print(s_msg) #user notification
                print("Transfer amount requested:\t", s_tran) #user notification
                print(u_msg) #user notification
                print(t_msg) #user notification
                print("Initial client account balance:\t", t_beg) #user notification
                print("Ending client account balance:\t", t_end) #user notification
                print(v_msg) #user notification

            except KeyError:
                s_msg = s["check_funds_message"]
                s_tran = s["tran_amount"]
                u_msg = u["transfer_account_message"]
                t_msg = t["transfer_withdraw_message"]
                v_msg = v["transfer_deposit_message"]
                print(s_msg) #user notification
                print("Transfer amount requested:\t", s_tran) #user notification
                print(u_msg) #user notification
                print(t_msg)  # user notification
                print(v_msg)  # user notification

            else:
                print("Please try your transaction again or see a teller for assistance")
                #insert a system alert for the bank to investigate any issues with the application


    def check_funds(self,args):
        self.__init__(self)
        #local variables
        account = args  #collect the acount number
        d_temp = {}  #will store all the results of this transaction
        msg = ""  #catch the results for the transaction log
        options = ["Checking", "checking", "Saving", "saving", ] #possible valid user entries for sub_account_type
        sub_acct = 0  # temp variable to fetch sub account number
        sub_acct_bal = 0  # temp variable for storing the sub accounts balances
        flag_sufficient_funds = bool  # flag to determine if the client has enough money to make desired transaction

        try:

            tran_amount = float(input("Please enter the amount you with to withdraw.\t")) #ask user for transaction amount


        except ValueError:
            msg = "Invalid withdrawal amount provided.  Please start again."
            d_temp["check_funds_message"] = msg
            d_temp["tran_amount"] = None
            return d_temp

        else:

            try:
                if tran_amount <= 0:
                    raise TypeError

            except TypeError:
                msg = "Invalid withdrawal amount provided.  Please start again."
                d_temp["check_funds_message"] = msg
                d_temp["tran_amount"] = tran_amount
                return d_temp

            else:
                d_temp["tran_amount"] = tran_amount
                sub_acct_type = input("Withdraw from checking or savings account? (Type checking or saving)") #ask what type of account they want to transact from
                try:
                    if sub_acct_type not in options:
                        raise TypeError
                except TypeError:
                    msg = "Invalid account type provided.  Please start again"
                    d_temp["check_funds_message"] = msg
                    return d_temp
                else:
                    d_temp["sub_account_type"] = sub_acct_type
                    for keys, values in self.account_details.items():  # look in client account dictionary
                        if keys == account:  # if the account number matches that of the client's account number
                            for k, v in values.items():  # look in the sub-dictionaries
                                if k == sub_acct_type:  # if the sub account type matches what was provided by the user
                                    sub_acct = v  # store the sub account number
                                    d_temp["sub_account"] = v #capture for transaction log
                                elif k == sub_acct:  # now that you have the sub account number, match to its key
                                    sub_acct_bal = v  # store the balance of the sub account
                                    d_temp["sub_account_balance_begin"] = v
                    try:
                         if sub_acct_bal < tran_amount: #check undesired outcome, there is less money in the account than the client's desired transaction amount
                             raise TypeError
                    except TypeError:
                         msg = "Insufficient funds available in the account client selected to complete client transaction. Please start again or see a Teller."
                         d_temp["check_funds_message"] = msg
                         flag_sufficient_funds = False
                         d_temp["flag_sufficient_funds"] = flag_sufficient_funds
                         return d_temp
                    else:
                        if sub_acct_bal >= tran_amount:  # verify if there is more money, or equal money, to the clients desired transaction
                             flag_sufficient_funds = True  # if there is, then set the flag equal to True
                             msg = "Sufficient funds available in client account to complete client transaction, proceed execute transaction."
                             d_temp["check_funds_message"] = msg
                             d_temp["flag_sufficient_funds"] = flag_sufficient_funds
                             return d_temp


    def withdraw_funds(self, args, kwargs):  #method to actually take funds from client account
        self.__init__(self)

        #local variables
        sub_acct_bal = 0  # variable to capture temporary starting balance of account
        temp_bal = 0  # variable to capture temporary calculated ending balance of account
        final_balance = 0  # variable to capture the final balance
        d_temp = {}
        msg = ""

        try:  #collect data from method input
            account = args
            d_check_funds = kwargs
            sub_account = d_check_funds["sub_account"]
            flag_funds = d_check_funds["flag_sufficient_funds"]
            tran_amount = d_check_funds["tran_amount"]

        except KeyError:  #if method input data incomplete, error message and leave method
            msg = "Issue with transaction data, withdrawal transaction not completed."
            d_temp["withdrawal_message"] = msg
            return d_temp

        else: #if input data found, proceed with method

            try:
                if flag_funds == False:
                    raise TypeError

            except TypeError:
                msg = "Insufficient funds, no withdrawal transaction processed."
                d_temp["withdrawal_message"] = msg
                return d_temp

            else:
                if flag_funds == True:
                    for keys, values in self.account_details.items():  #look into account details
                        if keys == account:
                            for k, v, in values.items():
                                if k == sub_account: #if the account matches the provided client sub account
                                    sub_acct_bal = v
                                    d_temp["withdrawal_begin_balance"] = v
                                    temp_bal = sub_acct_bal - tran_amount
                                    self.account_details[account][sub_account] = temp_bal
                                    final_balance = self.account_details[account][sub_account]
                                    d_temp["withdrawal_end_balance"] = final_balance
                                    msg = "Withdrawal from client account complete."
                                    d_temp["withdrawal_message"] = msg
                                    return d_temp



    def deposit_funds(self, args): #method for depositing funds, without a transfer
        self.__init__(self)
        account = args
        d_temp = {}
        msg = ""
        options = ["Checking", "checking", "Savings", "savings",]
        tran_amount = float(input("Please enter the amount you wish to deposit.")) #collect deposit amount
        try:
            if tran_amount <= 0:
                raise TypeError
        except TypeError:
            msg = "Incorrect deposit amount provided."
            #print(msg)
            d_temp["deposit_message"] = msg
            return d_temp
        else:
            d_temp["tran_amount"] = tran_amount
            sub_acct_type = input("Deposit to checking or savings account? (Type checking or saving)\t") #collect the type of account they wanted to deposit the funds to
            sub_acct_type.capitalize()
            try:
                if sub_acct_type not in options:
                    raise TypeError
            except TypeError:
                msg = "Incorrect account type provided."
                #print(msg)
                d_temp["deposit_message"] = msg
                return d_temp
            else:
                d_temp["sub_account_type"] = sub_acct_type
                sub_acct = 0 #placeholder for the sub account
                sub_acct_bal = 0 #placeholder for the starting balance fo the sub account
                temp_bal = 0 #placeholder for the calculate balance after the deposit
                final_balance = 0

                for keys, values in self.account_details.items(): #look into account details dictionary
                    if keys == account: #if the account equals that provided by the client
                        for k, v in values.items(): #look into the sub dictionaries
                            if k == sub_acct_type: #if the account type matches the type provided by client
                                sub_acct = v #store the sub account number
                                d_temp["sub_account"] = sub_acct #provide sub account number to transaction history temp
                            elif k == sub_acct: #now you have the sub account number, look at its contents
                                sub_acct_bal = v #collect the begining balance of the sub account
                                temp_bal = v + tran_amount #calculate the new balance, with clients deposit
                                d_temp["sub_account_balance_begin"] = sub_acct_bal #update transaction history temp with ending balance
                                self.account_details[account][k] = temp_bal #update actual sub account balance
                                final_balance = self.account_details[account][k] #collect final balance
                                d_temp["transaction_amount"] = tran_amount #update transaction amount in transaction history temp
                                d_temp["sub_account_balance_end"] = final_balance #update ending sub account balance in transaction history temp
                                msg = "Deposit was successful."
                                d_temp["deposit_message"] = msg
                return d_temp #return transaction log



    def transfer_account(self, kwargs): #method to verify if destination account provided by user for their transfer
        self.account_details #invoke account details

        #local variables
        options = ["Checking", "checking", "Saving", "saving", ]  # possible valid user entries for sub_account_type
        d_temp = {}  # placeholder for method results
        msg = ""  # placholder for transaction results message
        to_account = 0  # temp variable for the destination account
        to_sub_account_type = ""  # temp variable for the destination account type
        to_sub_account = 0  # temp variable for destination sub account
        flag_valid_transfer = bool
        flag_transfer_account = bool
        flag_transfer_sub_type = bool

        try:  #collect data from method inputs

            d_transfer_in = kwargs #collect input
            flag_funds = d_transfer_in["flag_sufficient_funds"]

        except KeyError: #if there is an issue with the input data, error message and leave method
            msg = "Issue with transaction data, transfer destination account not validated"
            d_temp["transfer_account_message"] = msg
            return d_temp

        else: #if input data is found, proceed with method

            try: #check the client had sufficient funds, if not, don't bother
                if flag_funds == False or flag_funds == None:
                    raise TypeError

            except TypeError:   #method action for undesirable outcome
                    msg = "Insufficient funds in client account, transfer not completed."
                    flag_valid_transfer = False
                    d_temp["transfer_account_message"] = msg
                    d_temp["check_transfer_flag"] = flag_valid_transfer
                    return d_temp #complete method

            else:  #next confirmations if funds are sufficient

                try:

                    if flag_funds == True:  #proceed only if funds were sufficient for the transfer
                        to_account = int(input("Please provide the account number to receive your transfer.\t"))  # get the destination account from the user


                except ValueError:
                       msg = "Provided transfer destination account cannot be processed"
                       d_temp["transfer_to_account"] = None  # update for transaction log
                       d_temp["transfer_account_message"] = msg  # update for transcation log
                       return d_temp

                else:
                    try:
                        d_temp["transfer_to_account"] = to_account  # update for transaction log
                        to_sub_account_type = input("Is it a checkings or savings account? Type checking or saving.\t")  # get the destination account type from the user


                    except ValueError: #undesirable outcome, client provided input cannot be processed as a string
                        msg = "Provided transfer destination account type cannot be processed"
                        d_temp["to_sub_account_type"] = None  # update for transaction log
                        d_temp["transfer_account_message"] = msg  # update for transcation log
                        return d_temp

                    else:

                        try:
                            d_temp["transfer_to_account"] = to_account  # update for transaction log
                            if to_sub_account not in options:
                                raise TypeError
                        except TypeError: #undesirable outcome that client provided input is an invalid account type
                            msg = "Provided transfer destination account type cannot be processed"
                            d_temp["to_sub_account_type"] = None  # update for transaction log
                            d_temp["transfer_account_message"] = msg  # update for transcation log
                            return d_temp

                        else:
                            d_temp["transfer_to_account"] = to_account  # update for transaction log
                            d_temp["to_sub_account_type"] = to_sub_account_type  # update for transcation log
                            for keys, values in self.account_details.items(): #look into dictionary to validate accounts
                                if keys == to_account: #look for the to_account ot be valid or not
                                    flag_transfer_account = True #if found, it's valid
                                    msg = "Transfer account confirmed." #message for transaction log
                                    d_temp["transfer_account_message"] = msg #update for transcation log
                                    for k, v, in values.items(): #look in sub dictionary for sub account type
                                        if k == to_sub_account_type: #look if sub account type is valid
                                            flag_transfer_sub_type = True #if found it's valid
                                            msg = "Transfer account sub type confirmed" #message for transaction log
                                            d_temp["transfer_sub_type_message"] = msg #update for transation log

                                try:  #check for undesirable outcome of incorrect account number provided
                                   if flag_transfer_account != True:
                                       raise TypeError

                                except TypeError: #action if account number invalid
                                       msg = "Unable to locate transfer to account."
                                       d_temp["transfer_account_message"] = msg
                                       flag_valid_transfer = False
                                       d_temp["check_transfer_flag"] = flag_valid_transfer
                                       return d_temp   #complete method

                                else: #method action if account number found to be valid, move on to check sub account type

                                    try: #if account valid, check for undesirable outcome of the sub account type does not exist
                                        if flag_transfer_sub_type != True:
                                            raise TypeError

                                    except TypeError:  #action if sub account type is not found
                                        msg = "Unable to locate the sub account type for transfer account."
                                        d_temp["transfer_sub_type_message"] = msg
                                        flag_valid_transfer = False
                                        d_temp["check_transfer_flag"] = flag_valid_transfer
                                        return d_temp  # complete method

                                    else: #if funds are sufficient, if to account is valid, is sub account type is valid, proceed to method action

                                        for keys, values in self.account_details.items(): #look in accounts dictionary
                                            if keys == to_account:  #check for account number
                                                for k, v, in values.items(): #look into sub dictionaries
                                                    if k == to_sub_account_type: #use the sub account type
                                                        to_sub_account = v #collect the sub account number in temporary variable
                                                        d_temp["to_sub_account"] = to_sub_account #add to transaction log
                                                        flag_valid_transfer = True #update confirmation flag
                                                        d_temp["check_transfer_flag"] = flag_valid_transfer #update to transaction log
                                                        return d_temp #complete method


    def transfer_deposit(self, kwargs_1, kwargs_2): #method to deposit the transfered amount to the desintation account
        self.__init__(self)

        # local variables
        d_temp = {}  # placeholder for transaction log from transfer deposit
        msg = ""  # placholder for message for transaction log
        to_sub_acct_bal = 0  # temp variable for collecting begining account balance of destination account
        temp_bal = 0  # temp variable for calculated balance after transfer deposit
        to_final_balance = 0  # temp variable to hold the final account balance

        try: #collect from method input

            d_in_check_funds = kwargs_1
            d_in_check_transfer = kwargs_2
            tran_amount = d_in_check_funds["tran_amount"]
            flag_funds = d_in_check_funds["flag_sufficient_funds"]
            to_account = d_in_check_transfer["transfer_to_account"]
            to_sub_account = d_in_check_transfer["to_sub_account"]
            flag_transfer = d_in_check_transfer["check_transfer_flag"]

        except KeyError:
            msg = "Issue with transaction data, transfer deposit not competed."
            d_temp["transfer_deposit_message"] = msg
            return d_temp

        else:

            try: #if the funds were found to be insufficient - no deposit to be made
                if flag_funds != True:
                    raise TypeError
                elif flag_transfer != True:
                    raise TypeError

            except TypeError: #method action for insufficient funds
                msg = "Insufficient funds or invalid destination account. Transfer deposit not completed"
                d_temp["transfer_deposit_message"] = msg
                return d_temp

            else: #the funds were sufficient and the transfer account was valid, proceed with deposit
                for keys, values in self.account_details.items():
                    if keys == to_account:
                        for k, v in values.items():
                            if k == to_sub_account:
                                sub_acct_bal = v
                                d_temp["to_account_balance_beg"] = v
                                temp_bal = sub_acct_bal + tran_amount
                                self.account_details[to_account][to_sub_account] = temp_bal
                                final_balance = self.account_details[to_account][to_sub_account]
                                d_temp["to_account_balance_end"] = final_balance
                                msg = "Transfer deposit successful."
                                d_temp["transfer_deposit_message"] = msg
                                return d_temp




    def transfer_withdraw(self, args, kwargs_1, kwargs_2):  # method to actually take funds from client account
        self.__init__(self)

        # local variables
        sub_acct_bal = 0  # variable to capture temporary starting balance of account
        temp_bal = 0  # variable to capture temporary calculated ending balance of account
        final_balance = 0  # variable to capture the final balance
        d_temp = {}
        msg = ""

        try:  # collect data from method input
            account = args
            d_check_funds = kwargs_1
            d_in_check_transfer = kwargs_2
            sub_account = d_check_funds["sub_account"]
            flag_funds = d_check_funds["flag_sufficient_funds"]
            tran_amount = d_check_funds["tran_amount"]
            flag_transfer = d_in_check_transfer["check_transfer_flag"]

        except KeyError:  # if method input data incomplete, error message and leave method
            msg = "Issue with transaction data, withdrawal transaction not completed."
            d_temp["transfer_withdraw_message"] = msg
            return d_temp

        else:  # if input data found, proceed with method

            try:
                if flag_funds != True or flag_transfer != True:
                    raise TypeError

            except TypeError:
                msg = "Insufficient funds or invalid transfer desination account, no withdrawal transaction processed."
                d_temp["transfer_withdraw_message"] = msg
                return d_temp

            else:
                if flag_funds == True:
                    for keys, values in self.account_details.items():  # look into account details
                        if keys == account:
                            for k, v, in values.items():
                                if k == sub_account:  # if the account matches the provided client sub account
                                    sub_acct_bal = v
                                    d_temp["transfer_withdraw_begin_balance"] = v
                                    temp_bal = sub_acct_bal - tran_amount
                                    self.account_details[account][sub_account] = temp_bal
                                    final_balance = self.account_details[account][sub_account]
                                    d_temp["transfer_withdraw_end_balance"] = final_balance
                                    msg = "Withdrawal from client account complete."
                                    d_temp["transfer_withdraw_message"] = msg
                                    return d_temp




    def check_balance(self, args): #method for allowing client ot check their balances
        self.__init__(self)

        #local variables
        d_temp = {}  # placeholder for account balance information
        msg = ""
        check_sub_account = 0
        savings_sub_account = 0

        try:
            account = args #collect account number

        except ValueError:
            msg = "Unable to process account information, balances not provided."
            d_temp["check_balance_message"] = msg
            return d_temp

        else:

            msg = "Account Information Accessed."
            d_temp["check_balance_message"] = msg

            try:
                check_sub_account = self.account_details[account]["checking"]  #collect sub account number

            except ValueError:
                msg = "Unable to process checking account, account may not exist."
                d_temp["checking_balance_message"] = msg


            else:
                msg = "Checking account confirmed."
                d_temp["checking_balance_message"] = msg

                try:
                    d_temp["checking_balance_amount"] = self.account_details[account][check_sub_account]  # create key:value, store balance, for results

                except ValueError:
                    msg = "Error in retrieving account balance for checking account. Please see Teller."
                    d_temp["checking_balance_amount"] = None
                    d_temp["checking_balance_message"] = msg

                else:
                    try:
                        savings_sub_account = self.account_details[account]["saving"]  # collect sub account number

                    except ValueError:
                        msg = "Unable to process savings account, account may not exist."
                        d_temp["saving_balance_message"] = msg

                    else:
                        msg = "Savings account confirmed."
                        d_temp["saving_balance_message"] = msg

                        try:
                            d_temp["saving_balance_amount"] = self.account_details[account][savings_sub_account]  # create key:value, store balance, for results

                        except ValueError:
                            msg = "Error in retrieving account balance for savings account. Please see Teller."
                            d_temp["saving_balance_message"] = msg

                        else:
                             return d_temp #return temporary dictionaries for client notification


class Client:

    def client_atm(self):
        b = ATMConfirmClient  # invoke class for confirming the client identity
        c = int(input("Please provide your card number.\t"))  # collect client card/account number
        p = int(input("Please enter your pin number.\t"))  # collect client pin number
        d_user = {}  # placeholder to store user input
        d_user["user_account"] = c  # key:value pair for user input of account/card number
        d_user["user_pin"] = p  # key:value pair for user input of personal identification number
        confirmation = {}  # placeholder of check_account and check_pin method results
        confirmation = ATMConfirmClient.atm_check_account(b, d_user)  # call class method and set temp variable for confirming client account identify
        flag_account = confirmation["flag_account"]  # retrieve confirmation flag for account number
        flag_pin = confirmation["flag_pin"]  # retrieve confirmation flag for pin number

        try:  # evaluate undesired outcome
            if flag_account != True or flag_pin != True:
                raise TypeError
        except TypeError:  # action for undesired outcome
            print("Apologies but we cannot complete your desired transactions.")
            print("Please visit the Teller.")
            exit()
        else:  # action for desired outcome
            while True:
                choice = input("For a new transaction, type N. To Exit, type E.")

                if choice == "n" or choice == "N":
                    e = ServiceSelection  # invoke class for making client transaction selection
                    d_tran = ServiceSelection.transaction_type(
                        e)  # call class method and setting temporary variable for selection made
                    f = Transactions
                    Transactions.atm_transaction_calls(f, d_user, d_tran)
                elif choice == "E" or choice =="e":
                    print("Thank you.")
                    exit()
                else:
                    print("Invalid selection.")
                    exit()

    def client_bank(self):
        b = ConfirmBankTeller  # invoke class for confirming the client identity
        c = input("Please enter username.\t")  # collect client card/account number
        p = input("Please enter your password.\t")  # collect client pin number
        d_login = {}  # placeholder to store user input
        d_login["username"] = c  # key:value pair for user input of account/card number
        d_login["password"] = p  # key:value pair for user input of personal identification number
        confirm_login = {}  # placeholder of check_account and check_pin method results
        confirm_login = ConfirmBankTeller.check_user(b, d_login)
        flag_user = confirm_login["flag_user"]
        flag_password = confirm_login["flag_password"]

        try:
            if flag_user != True or flag_password != True:
                raise TypeError

        except TypeError:
            print("Invalid credentials.")
            exit()

        else:
            while True:
                bank_choice = input("To start a new transaction, type New, or to exit, type Exit.\t")
                if bank_choice == "New" or bank_choice == "new":

                    try:
                        e = int(input("Please provide the debit card number."))

                    except ValueError:
                        print("Invalid entry for account numbers")
                        exit()

                    else:
                        confirm_login["client_account"] = e
                        g = ServiceSelection  # invoke class for making client transaction selection
                        d_tran = ServiceSelection.transaction_type(
                            g)  # call class method and setting temporary variable for selection made
                        f = Transactions
                        h = Transactions.bank_transaction_calls(f, confirm_login, d_tran)

                elif bank_choice == "exit" or bank_choice == "Exit":
                    print("Thank you.")
                    exit()
                else:
                    print("Invalid selection.")
                    exit()

    def client_teller(self):
        b = ConfirmBankTeller  # invoke class for confirming the client identity
        c = input("Please enter username.\t")  # collect client card/account number
        p = input("Please enter your password.\t")  # collect client pin number
        d_login = {}  # placeholder to store user input
        d_login["username"] = c  # key:value pair for user input of account/card number
        d_login["password"] = p  # key:value pair for user input of personal identification number
        confirm_login = {}  # placeholder of check_account and check_pin method results
        confirm_login = ConfirmBankTeller.check_user(b, d_login)
        flag_user = confirm_login["flag_user"]
        flag_password = confirm_login["flag_password"]
        try:
            if flag_user != True or flag_password != True:
                raise TypeError

        except TypeError:
            print("Invalid credentials.")
            exit()

        else:
            while True:
                teller_choice = input("To start a new transaction, type New, or to exit, type Exit.\t")
                if teller_choice == "New" or teller_choice == "new":

                    try:
                        e = int(input("Please provide the debit card number."))

                    except ValueError:
                        print("Invalid entry for account numbers")
                        exit()

                    else:
                        confirm_login["client_account"] = e
                        g = ServiceSelection  # invoke class for making client transaction selection
                        d_tran = ServiceSelection.transaction_type(g)  # call class method and setting temporary variable for selection made
                        f = Transactions
                        h = Transactions.teller_transaction_calls(f, confirm_login, d_tran)

                elif teller_choice == "exit" or teller_choice == "Exit":
                    print("Thank you.")
                    exit()
                else:
                    print("Invalid selection.")
                    exit()



def main():
    run_mode = input("Please provide the run mode. (B = bank, T = teller, C = Client ATM)")
    try:
        options = ["B", "b", "T", "t", "c", "C",]
        if run_mode not in options:
            raise TypeError
    except TypeError:
        print("Invalid selection.")
        exit()
    else:
        if run_mode == "C" or run_mode == "c":
            x = Client()
            y = Client.client_atm(x)

        elif run_mode =="B" or run_mode == "b":
            x = Client()
            y = Client.client_bank(x)

        elif run_mode =="T" or run_mode == "t":
            x = Client()
            y = Client.client_teller(x)
        else:
            print("Invalid selection.")
            exit()



if __name__ == "__main__":
    main() #call main function
