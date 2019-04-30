import datetime

#integrating the usage of files instead of dictionaries
#everything works

#Done
#source data from files
#write transaction data to transaction history file
#incorporate time stamp to tran history keys

# TO DO
#write updates to account data after transactions


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

class Files:

    def read_client_authentication_file(fname):
        client_file = open(fname, "r")
        d_temp = {}
        d = {}
        d_input = {}

        try:

            for line in client_file:
                field = line.split(";")
                d = {}
                d_temp = {}
                d_temp[str(field[1])] = int(field[2])
                d[int(field[0])] = d_temp
                d_input.update(d)
        except IOError:
            print("Error 101: client authentication file unavailable.")

        finally:
            client_file.close()
            return d_input


    def read_firm_authentication_file(fname):
        firm_file = open(fname, "r")
        d_temp = {}
        d = {}
        d_input = {}

        try:

            for line in firm_file:
                field = line.split(";")
                d = {}
                d_temp = {}
                d_temp[field[1]] = field[2].replace("\n", "")
                d[field[0]] = d_temp
                d_input.update(d)
        except IOError:
            print("Error 102: firm authentication file unavailable.")

        finally:
            firm_file.close()
            return d_input


    def read_account_file(fname1, fname2):
        data_file = open(fname1, "r")
        header_file = open(fname2, "r")

        header = []
        d_temp = {}
        d_t = {}
        d_input = {}
        g = {}

        try:

            for line in header_file:
                header = line.split(";")

        except IOError:
            print("Error 103: account header file unavailable.")

        try:

            for line in data_file:
                field = line.split(";")
                field.pop()
                for i in range(len(field)):
                    d_t = {}
                    g[header[i]] = field[i]
                    d_t.update(g)
                    d_temp[field[0]] = d_t
                    d_input.update(d_temp)

        except IOError:
            print("Error 104: account detail file unavailable.")

        finally:
            header_file.close()
            data_file.close()
        return (d_input)


    def update_transaction_history_file(fname, *args):
        tran_hist = open(fname, "a+")

        try:
            for arg in args:
                print(arg)
                now = datetime.datetime.now()
                timestamp = datetime.datetime.timestamp(now)
                t = str(timestamp) + str(arg)
                tran_hist.write(t + '\n')
        except IOError:
            print("Error 105: transaction history file not found.")

        finally:
            #        for lines in tran_hist: #developer check
            #            print(lines) #developer check
            tran_hist.close()


class ATMConfirmClient: #class to verify the identify of the client attempting to user ATM
    def __init__(self):
        # dictionary of client accounts and their personal identification number (pin)
        a = Files.read_client_authentication_file("client_authentication.txt")
        self.accounts = {}
        self.accounts.update(a)


    def atm_check_account(self, kwargs): #method to confirm existance of the client
        self.__init__(self) #invoke account dictionary
        self.accounts
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
            msg_temp = "Error 106: Pin could not be confirmed."  #message for transaction log
        d_temp_response["flag_pin"]=flag_pin  #create key:value pair for method response
        d_temp_response["msg_pin"]=msg_temp   #create key:value pair for method response
        return d_temp_response #return confirmation of personal identification number


class ConfirmBankTeller: #class to verify the identify of the firm party log in
    def __init__(self):
        # file call for log in details
        x = Files
        y = Files.read_firm_authentication_file("firm_authentication.txt")
        self.users = {}
        self.users.update(y)
        #print(self.users)
        #print("in init", self.users)


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
            msg_user = "Error 107: Issue experienced with log in data, user not validated"
            #print(msg_user)
            flag_user = None
            msg_password = "Error 108: Issue experienced with log in data, password not validated"
            #print(msg_password)
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
                msg_password = "Error 109: User name not confirmed, password not validated"
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
            msg_password = "Error 110: Issue experienced with log in data, password not validated"
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
                msg_password = "Error 111: User password could not be validated."
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
            print("Error 112: Invalid transaction selected.")
            print("Please visit the teller for assistance")
            exit()
        else: #action for desired outcome
            return d_temp


class Transactions: #class for all transaction types supported


    def __init__(self):

        x = Files()
        y = Files.read_account_file("accounts.txt", "headers_accounts.txt")
        #w = Files.update_transaction_history_file("transaction_history.txt", *args)

        k =""
        #k =datetime.datetime.now()
        #print(k)

        self.account_details1 = {}
        self.tran_history = {}
        self.account_details1.update(y)
        print(self.account_details1)



    def teller_transaction_calls(self, user, tran):
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1


        account = user["client_account"]
        tran = tran["tran_type"]
        if tran == "D": #should add additional logic to help prevent failures and illogical values
            t = Transactions.deposit_funds(self, account) #call transaction method for depositing funds into an account
            self.tran_history[5.1] = user
            self.tran_history[5.2] = tran
            self.tran_history[5.3] = t
            k = datetime.datetime.now()  #get system time stamp
            o = (k.timestamp(),5.1,user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(),5.2,tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(),5.3,t)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m, n)  # append transaction history to main transaction history dictionary


            print(self.tran_history.items())
            t_msg = t["deposit_message"]
            try:
                t_1 = t["sub_account_balance_begin"]
                t_2 = t["transaction_amount"]
                t_3 = t["sub_account_balance_end"]
            except KeyError:
                print("Error 113: Transaction issue, please escalate.")
                #insert a system alert to notify the Bank to investigate any issues
            else:
                print("The account balance before deposit:\t", t_1) #confirm transactiont to user
                print("The deposit amount:\t", t_2) #confirm transactiont to user
                print("The account balance after deposit:\t", t_3) #confirm transactiont to user
        elif tran == "C": #should add additional logic to help prevent failures and illogical values
            t = Transactions.check_balance(self, account) #call transaction method to check balances
            self.tran_history[4.1] = user  #append transaction history to main transaction history dictionrary
            self.tran_history[4.2] = tran  #append transaction history to main transaction history dictionrary
            self.tran_history[4.3] = t  #update transaction history with contents of checking account balances
            print(self.tran_history.items())

            k = datetime.datetime.now()  #get system time stamp
            o = (k.timestamp(),4.1,user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(),4.2,tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(),4.3,t)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m, n)  # append transaction history to main transaction history dictionary

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
                        print("Error 114: Technical issues accessing account information, please escalate.")
        elif tran == "W": #should add additional logic to help prevent failures and illogical values
            s = Transactions.check_funds(self, account) #method call, confirm client has sufficient funds
            t = Transactions.withdraw_funds(self, account, s)  # method call to complete the withdrawal
            self.tran_history[6] = user  # append transaction history to main transaction history dictionary
            self.tran_history[6.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[6.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[6.3]= t # append transaction history to main transaction history dictionary

            k = datetime.datetime.now()  #get system time stamp
            o = (k.timestamp(),6.1,user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(),6.2,tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(),6.3,s)  # append transaction history to main transaction history dictionary
            p = (k.timestamp(),6.4,t)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m, n, p)  # append transaction history to main transaction history dictionary



            try:
                s_msg = s["check_funds_message"]
                s_tran = s["tran_amount"]
                t_msg = t["withdrawal_message"]
                t_beg = t["withdrawal_begin_balance"]
                t_end = t["withdrawal_end_balance"]
            except KeyError:
                print("Error 115: Issue with transaction, please escalate.")
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

            k = datetime.datetime.now()  #get system time stamp
            o = (k.timestamp(),8.1,user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(),8.2,tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(),8.3,s)  # append transaction history to main transaction history dictionary
            p = (k.timestamp(),8.4,u)  # append transaction history to main transaction history dictionary
            q = (k.timestamp(),8.5,t)  # append transaction history to main transaction history dictionary
            r = (k.timestamp(),8.6,v)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m, n, p, q, r)  # append transaction history to main transaction history dictionary



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
                print("Error 116: Issue with transaction, please escalate")
                #insert a system alert for the bank to investigate any issues with the application


    def bank_transaction_calls(self, user, tran):
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1


        account = user["client_account"]
        tran = tran["tran_type"]
        if tran == "D": #should add additional logic to help prevent failures and illogical values
            t = Transactions.deposit_funds(self, account) #call transaction method for depositing funds into an account
            self.tran_history[5.1] = user
            self.tran_history[5.2] = tran
            self.tran_history[5.3] = t
            print(self.tran_history.items())

            k = datetime.datetime.now()  # get system time stamp
            o = (k.timestamp(), 5.1, user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(), 5.2, tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(), 5.3, t)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m,n)  # append transaction history to main transaction history dictionary

        elif tran == "C": #should add additional logic to help prevent failures and illogical values
            t = Transactions.check_balance(self, account) #call transaction method to check balances
            self.tran_history[4.1] = user  #append transaction history to main transaction history dictionrary
            self.tran_history[4.2] = tran  #append transaction history to main transaction history dictionrary
            self.tran_history[4.3] = t  #update transaction history with contents of checking account balances
            print(self.tran_history.items())

            k = datetime.datetime.now()  # get system time stamp
            o = (k.timestamp(), 4.1, user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(), 4.2, tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(), 4.3, t)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m,n)  # append transaction history to main transaction history dictionary

        elif tran == "W": #should add additional logic to help prevent failures and illogical values
            s = Transactions.check_funds(self, account) #method call, confirm client has sufficient funds
            t = Transactions.withdraw_funds(self, account, s)  # method call to complete the withdrawal
            self.tran_history[6] = user  # append transaction history to main transaction history dictionary
            self.tran_history[6.1]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[6.2] = s  # append transaction history to main transaction history dictionary
            self.tran_history[6.3]= t # append transaction history to main transaction history dictionary
            print(self.tran_history.items()) #developer check
            k = datetime.datetime.now()  # get system time stamp
            o = (k.timestamp(), 6.1, user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(), 6.2, tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(), 6.3, s)  # append transaction history to main transaction history dictionary
            p = (k.timestamp(), 6.4, t)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m, n,p)  # append transaction history to main transaction history dictionary

        elif tran == "T": #should add additional logic to help prevent failures and illogical values

            s = Transactions.check_funds(self, account) #method call to confirm client has sufficient fund
            u = Transactions.transfer_account(self, s) #method call to confirm destination account
            t = Transactions.transfer_withdraw(self, account, s, u) #method call to withdrawl funds from client account
            v = Transactions.transfer_deposit(self, s, u) #method call to deposit transfer amount in destination account
            self.tran_history[8.1] = user  # append transaction history to main transaction history dictionary
            self.tran_history[8.2]= tran  # append transaction history to main transaction history dictionary
            self.tran_history[8.3] = s  # append transaction history to main transaction history dictionary
            self.tran_history[8.4]= u # append transaction history to main transaction history dictionary
            self.tran_history[8.5] = t  # append transaction history to main transaction history dictionary
            self.tran_history[8.6] = v  # append transaction history to main transaction history dictionary
            print(self.tran_history.items())
            k = datetime.datetime.now()  # get system time stamp
            o = (k.timestamp(), 8.1, user)  # append transaction history to main transaction history dictionary
            m = (k.timestamp(), 8.2, tran)  # append transaction history to main transaction history dictionary
            n = (k.timestamp(), 8.3, s)  # append transaction history to main transaction history dictionary
            p = (k.timestamp(), 8.4, u)  # append transaction history to main transaction history dictionary
            q = (k.timestamp(), 8.5, t)  # append transaction history to main transaction history dictionary
            r = (k.timestamp(), 8.6, v)  # append transaction history to main transaction history dictionary
            w = Files.update_transaction_history_file("transaction_history.txt", o, m, n, p, q,r)  # append transaction history to main transaction history dictionary


    def atm_transaction_calls(self, user, tran):
            self.__init__(self)
            #self.tran_history
            #self.account_details
            #self.account_details1

            account = user["user_account"]
            tran = tran["tran_type"]
            if tran == "D": #should add additional logic to help prevent failures and illogical values
                t = Transactions.deposit_funds(self, account) #call transaction method for depositing funds into an account
                self.tran_history[5.1] = user
                self.tran_history[5.2] = tran
                self.tran_history[5.3] = t
                print(self.tran_history.items())
                k = datetime.datetime.now()  # get system time stamp
                o = (k.timestamp(), 5.1, user)  # append transaction history to main transaction history dictionary
                m = (k.timestamp(), 5.2, tran)  # append transaction history to main transaction history dictionary
                n = (k.timestamp(), 5.3, t)  # append transaction history to main transaction history dictionary
                w = Files.update_transaction_history_file("transaction_history.txt", o, m,n)  # append transaction history to main transaction history dictionary

                t_msg = t["deposit_message"]
                print(t_msg)  # confirm transaction to user
                try:
                    t_1 = t["sub_account_balance_begin"]
                    t_2 = t["transaction_amount"]
                    t_3 = t["sub_account_balance_end"]
                except KeyError:
                    print("Error 117: Please try your transaction again or see a Teller for assistance.")
                    #insert a system alert to notify the Bank to investigate any issues
                else:
                    print("Your account balance before your deposit:\t", t_1) #confirm transactiont to user
                    print("Your deposit amount:\t", t_2) #confirm transactiont to user
                    print("Your account balance after your deposit:\t", t_3) #confirm transactiont to user
            elif tran == "C": #should add additional logic to help prevent failures and illogical values
                t = Transactions.check_balance(self, account) #call transaction method to check balances
                self.tran_history[4.1] = user  #append transaction history to main transaction history dictionrary
                self.tran_history[4.2] = tran  #append transaction history to main transaction history dictionrary
                self.tran_history[4.3] = t  #update transaction history with contents of checking account balances
                print(self.tran_history.items())

                k = datetime.datetime.now()  # get system time stamp
                o = (k.timestamp(), 4.1, user)  # append transaction history to main transaction history dictionary
                m = (k.timestamp(), 4.2, tran)  # append transaction history to main transaction history dictionary
                n = (k.timestamp(), 4.3, t)  # append transaction history to main transaction history dictionary
                w = Files.update_transaction_history_file("transaction_history.txt", o, m, n)  # append transaction history to main transaction history dictionary

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
                            print("Error 118: Technical issues with accessing your account information, please see teller.")
            elif tran == "W": #should add additional logic to help prevent failures and illogical values
                s = Transactions.check_funds(self, account) #method call, confirm client has sufficient funds
                t = Transactions.withdraw_funds(self, account, s)  # method call to complete the withdrawal
                self.tran_history[6] = user  # append transaction history to main transaction history dictionary
                self.tran_history[6.1]= tran  # append transaction history to main transaction history dictionary
                self.tran_history[6.2] = s  # append transaction history to main transaction history dictionary
                self.tran_history[6.3]= t # append transaction history to main transaction history dictionary

                k = datetime.datetime.now()  # get system time stamp
                o = (k.timestamp(), 6.1, user)  # append transaction history to main transaction history dictionary
                m = (k.timestamp(), 6.2, tran)  # append transaction history to main transaction history dictionary
                n = (k.timestamp(), 6.3, s)  # append transaction history to main transaction history dictionary
                p = (k.timestamp(), 6.4, t)  # append transaction history to main transaction history dictionary
                w = Files.update_transaction_history_file("transaction_history.txt", o, m, n, p)  # append transaction history to main transaction history dictionary

                try:
                    s_msg = s["check_funds_message"]
                    s_tran = s["tran_amount"]
                    t_msg = t["withdrawal_message"]
                    t_beg = t["withdrawal_begin_balance"]
                    t_end = t["withdrawal_end_balance"]
                except KeyError:
                    print("Error 119: Please try your transaction again or see a teller for assistance")
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
                print("check funds succeeded.")
                u = Transactions.transfer_account(self, s) #method call to confirm destination account
                print("transfer account succeeded")
                t = Transactions.transfer_withdraw(self, account, s, u) #method call to withdrawl funds from client account
                print("transfer withdrawal succeeded")
                v = Transactions.transfer_deposit(self, s, u) #method call to deposit transfer amount in destination account
                print("transfer deposit succeeded")
                self.tran_history[8.1] = user  # append transaction history to main transaction history dictionary
                self.tran_history[8.2]= tran  # append transaction history to main transaction history dictionary
                self.tran_history[8.3] = s  # append transaction history to main transaction history dictionary
                self.tran_history[8.4]= u # append transaction history to main transaction history dictionary
                self.tran_history[8.5] = t  # append transaction history to main transaction history dictionary
                self.tran_history[8.6] = v  # append transaction history to main transaction history dictionary

                k = datetime.datetime.now()  # get system time stamp
                o = (k.timestamp(), 8.1, user)  # append transaction history to main transaction history dictionary
                m = (k.timestamp(), 8.2, tran)  # append transaction history to main transaction history dictionary
                n = (k.timestamp(), 8.3, s)  # append transaction history to main transaction history dictionary
                p = (k.timestamp(), 8.4, u)  # append transaction history to main transaction history dictionary
                q = (k.timestamp(), 8.5, t)  # append transaction history to main transaction history dictionary
                r = (k.timestamp(), 8.6, v)  # append transaction history to main transaction history dictionary
                w = Files.update_transaction_history_file("transaction_history.txt", o, m, n, p, q,r)  # append transaction history to main transaction history dictionary

                try:
                        s_msg = s["check_funds_message"]
                        #print("test1", s_msg)
                        s_tran = s["tran_amount"]
                        #print("test2",s_tran)
                        u_msg = u["transfer_account_message"]
                        #print("test3",u_msg)
                        t_msg = t["transfer_withdraw_message"]
                        #print("test4",t_msg)
                        t_beg = t["transfer_withdraw_begin_balance"]
                        #print("test5",t_beg)
                        t_end = t["transfer_withdraw_end_balance"]
                        #print("test6",t_end)
                        v_msg = v["transfer_deposit_message"]
                        #print("test7",v_msg)



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
                    print(s_msg)  # user notification
                    print("Transfer amount requested:\t", s_tran)  # user notification
                    print(u_msg)  # user notification
                    print(t_msg)  # user notification
                    print("Initial client account balance:\t", t_beg)  # user notification
                    print("Ending client account balance:\t", t_end)  # user notification
                    print(v_msg)  # user notification


    def check_funds(self,args):
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1



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
            msg = "Error 120: Invalid withdrawal amount provided.  Please start again."
            d_temp["check_funds_message"] = msg
            d_temp["tran_amount"] = None
            print(d_temp)
            return d_temp

        else:

            try:
                if tran_amount <= 0:
                    raise TypeError

            except TypeError:
                msg = "Error 121: Invalid withdrawal amount provided.  Please start again."
                d_temp["check_funds_message"] = msg
                d_temp["tran_amount"] = tran_amount
                print(d_temp)
                return d_temp

            else:
                d_temp["tran_amount"] = tran_amount
                sub_acct_type = input("Withdraw from checking or savings account? (Type checking or saving)") #ask what type of account they want to transact from
                try:
                    if sub_acct_type not in options:
                        raise TypeError
                except TypeError:
                    msg = "Error 122: Invalid account type provided.  Please start again"
                    d_temp["check_funds_message"] = msg
                    print(d_temp)
                    return d_temp
                else:
                    d_temp["sub_account_type"] = sub_acct_type
                    if sub_acct_type == "checking":
                        for keys, values in self.account_details1.items():  # look in client account dictionary
                            if keys == str(account):  # if the account number matches that of the client's account number
                                for k, v in values.items():  # look in the sub-dictionaries
                                    if k == "checking_account_number":  # if the sub account type matches what was provided by the user
                                        sub_acct = v  # store the sub account number
                                        d_temp["sub_account"] = v #capture for transaction log
                                    elif k == "checking_balance":  # now that you have the sub account number, match to its key
                                        sub_acct_bal = float(v)  # store the balance of the sub account
                                        d_temp["sub_account_balance_begin"] = v
                    elif sub_acct_type == "saving":
                        for keys, values in self.account_details1.items():  # look in client account dictionary
                            if keys == str(account):  # if the account number matches that of the client's account number
                                for k, v in values.items():  # look in the sub-dictionaries
                                    if k == "saving_account_number":  # if the sub account type matches what was provided by the user
                                        sub_acct = v  # store the sub account number
                                        d_temp["sub_account"] = v #capture for transaction log
                                    elif k == "saving_balance":  # now that you have the sub account number, match to its key
                                        sub_acct_bal = float(v)  # store the balance of the sub account
                                        d_temp["sub_account_balance_begin"] = v
                    try:
                         if sub_acct_bal < tran_amount: #check undesired outcome, there is less money in the account than the client's desired transaction amount
                             raise TypeError
                    except TypeError:
                         msg = "Error 123: Insufficient funds available in the account client selected to complete client transaction. Please start again or see a Teller."
                         d_temp["check_funds_message"] = msg
                         flag_sufficient_funds = False
                         d_temp["flag_sufficient_funds"] = flag_sufficient_funds
                         print(d_temp)
                         return d_temp
                    else:
                        if sub_acct_bal >= tran_amount:  # verify if there is more money, or equal money, to the clients desired transaction
                             flag_sufficient_funds = True  # if there is, then set the flag equal to True
                             msg = "Sufficient funds available in client account to complete client transaction, proceed execute transaction."
                             d_temp["check_funds_message"] = msg
                             d_temp["flag_sufficient_funds"] = flag_sufficient_funds
                             print(d_temp)
                             return d_temp


    def withdraw_funds(self, args, kwargs):  #method to actually take funds from client account
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1

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
            sub_account_type = d_check_funds["sub_account_type"]
            flag_funds = d_check_funds["flag_sufficient_funds"]
            tran_amount = d_check_funds["tran_amount"]

        except KeyError:  #if method input data incomplete, error message and leave method
            msg = "Error 124: Issue with transaction data, withdrawal transaction not completed."
            d_temp["withdrawal_message"] = msg
            print(d_temp)
            return d_temp

        else: #if input data found, proceed with method

            try:
                if flag_funds == False:
                    raise TypeError

            except TypeError:
                msg = "Error 125: Insufficient funds, no withdrawal transaction processed."
                d_temp["withdrawal_message"] = msg
                return d_temp

            else:
                if flag_funds == True and sub_account_type == "checking":
                    for keys, values in self.account_details1.items():  #look into account details
                        if keys == str(account):
                            for k, v, in values.items():
                                if k == "checking_balance": #if the account matches the provided client sub account
                                    sub_acct_bal = float(v)
                                    d_temp["withdrawal_begin_balance"] = v
                                    temp_bal = sub_acct_bal - tran_amount
                                    self.account_details1[str(account)]["checking_balance"] = temp_bal
                                    final_balance = self.account_details1[str(account)]["checking_balance"]
                                    d_temp["withdrawal_end_balance"] = final_balance
                                    msg = "Withdrawal from client account complete."
                                    d_temp["withdrawal_message"] = msg
                                    print(d_temp)
                                    return d_temp
                elif flag_funds == True and sub_account_type == "saving":
                    for keys, values in self.account_details1.items():  #look into account details
                        if keys == str(account):
                            for k, v, in values.items():
                                if k == "saving_balance": #if the account matches the provided client sub account
                                    sub_acct_bal = float(v)
                                    d_temp["withdrawal_begin_balance"] = v
                                    temp_bal = sub_acct_bal - tran_amount
                                    self.account_details1[str(account)]["saving_balance"] = temp_bal
                                    final_balance = self.account_details1[str(account)]["saving_balance"]
                                    d_temp["withdrawal_end_balance"] = final_balance
                                    msg = "Withdrawal from client account complete."
                                    d_temp["withdrawal_message"] = msg
                                    print(d_temp)
                                    return d_temp


    def deposit_funds(self, args): #method for depositing funds, without a transfer
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1

        account = args
        d_temp = {}
        msg = ""
        options = ["Checking", "checking", "Saving", "saving",]
        tran_amount = float(input("Please enter the amount you wish to deposit.")) #collect deposit amount
        try:
            if tran_amount <= 0:
                raise TypeError
        except TypeError:
            msg = "Incorrect deposit amount provided."
            #print(msg)
            d_temp["deposit_message"] = msg
            print(d_temp)
            return d_temp
        else:
            d_temp["tran_amount"] = tran_amount
            sub_acct_type = input("Deposit to checking or savings account? (Type checking or saving)\t") #collect the type of account they wanted to deposit the funds to
            sub_acct_type.lower()
            print(sub_acct_type)
            try:
                if sub_acct_type not in options:
                    raise TypeError
            except TypeError:
                msg = "Incorrect account type provided."
                print(msg)
                d_temp["deposit_message"] = msg
                print(d_temp)
                return d_temp
            else:
                d_temp["sub_account_type"] = sub_acct_type
                sub_acct = 0 #placeholder for the sub account
                sub_acct_bal = 0 #placeholder for the starting balance fo the sub account
                temp_bal = 0 #placeholder for the calculate balance after the deposit
                final_balance = 0

                if sub_acct_type == "checking":
                    for keys, values in self.account_details1.items(): #look into account details dictionary
                        if keys == str(account): #if the account equals that provided by the client
                            for k, v in values.items(): #look into the sub dictionaries
                                if k == "checking_account_number": #if the account type matches the type provided by client
                                    sub_acct = v #store the sub account number
                                    d_temp["sub_account"] = sub_acct #provide sub account number to transaction history temp
                                elif k == "checking_balance": #now you have the sub account number, look at its contents
                                    sub_acct_bal = float(v) #collect the begining balance of the sub account
                                    temp_bal = float(v) + tran_amount #calculate the new balance, with clients deposit
                                    d_temp["sub_account_balance_begin"] = sub_acct_bal #update transaction history temp with ending balance
                                    self.account_details1[str(account)][k] = temp_bal #update actual sub account balance
                                    final_balance = self.account_details1[str(account)][k] #collect final balance
                                    d_temp["transaction_amount"] = tran_amount #update transaction amount in transaction history temp
                                    d_temp["sub_account_balance_end"] = final_balance #update ending sub account balance in transaction history temp
                                    msg = "Deposit was successful."
                                    d_temp["deposit_message"] = msg
                                    print(d_temp)
                                    return(d_temp)
                elif sub_acct_type == "saving":
                    for keys, values in self.account_details1.items(): #look into account details dictionary
                        if keys == str(account): #if the account equals that provided by the client
                            for k, v in values.items(): #look into the sub dictionaries
                                if k == "saving_account_number": #if the account type matches the type provided by client
                                    sub_acct = v #store the sub account number
                                    d_temp["sub_account"] = sub_acct #provide sub account number to transaction history temp
                                elif k == "saving_balance": #now you have the sub account number, look at its contents
                                    sub_acct_bal = float(v) #collect the begining balance of the sub account
                                    temp_bal = float(v) + tran_amount #calculate the new balance, with clients deposit
                                    d_temp["sub_account_balance_begin"] = sub_acct_bal #update transaction history temp with ending balance
                                    self.account_details1[str(account)][k] = temp_bal #update actual sub account balance
                                    final_balance = self.account_details1[str(account)][k] #collect final balance
                                    d_temp["transaction_amount"] = tran_amount #update transaction amount in transaction history temp
                                    d_temp["sub_account_balance_end"] = final_balance #update ending sub account balance in transaction history temp
                                    msg = "Deposit was successful."
                                    d_temp["deposit_message"] = msg
                                    print(d_temp)
                                    return(d_temp)
                print(d_temp)
                return d_temp #return transaction log


    def transfer_account(self, kwargs): #method to verify if destination account provided by user for their transfer
        self.__init__(self)
        #self.account_details #invoke account details
        #self.tran_history
        #self.account_details
        #self.account_details1

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
            msg = "Error 125: Issue with transaction data, transfer destination account not validated"
            d_temp["transfer_account_message"] = msg
            return d_temp

        else: #if input data is found, proceed with method

            try: #check the client had sufficient funds, if not, don't bother
                if flag_funds == False or flag_funds == None:
                    raise TypeError

            except TypeError:   #method action for undesirable outcome
                    msg = "Error 126: Insufficient funds in client account, transfer not completed."
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
                            if to_sub_account_type not in options:
                                raise TypeError
                        except TypeError: #undesirable outcome that client provided input is an invalid account type
                            msg = "Error 126: Provided transfer destination account type cannot be processed"
                            d_temp["to_sub_account_type"] = None  # update for transaction log
                            d_temp["transfer_account_message"] = msg  # update for transcation log
                            print("1:", d_temp)
                            return d_temp

                        else:
                            d_temp["transfer_to_account"] = to_account  # update for transaction log
                            d_temp["to_sub_account_type"] = to_sub_account_type  # update for transcation log
                            if to_sub_account_type == "checking":
                                for keys, values in self.account_details1.items(): #look into dictionary to validate accounts
                                    if keys == str(to_account): #look for the to_account ot be valid or not
                                        flag_transfer_account = True #if found, it's valid
                                        print(flag_transfer_account)
                                        msg = "Transfer account confirmed." #message for transaction log
                                        d_temp["transfer_account_message"] = msg #update for transcation log
                                        for k, v, in values.items(): #look in sub dictionary for sub account type
                                            if k == "checking_account_number": #look if sub account type is valid
                                                msg = "Transfer account sub type confirmed" #message for transaction log
                                                d_temp["transfer_sub_type_message"] = msg #update for transation log
                                                flag_transfer_sub_type = True  # update confirmation flag
                                                d_temp["flag_transfer_sub_account"] = flag_transfer_sub_type  # update for transation log
                                                print("2:", d_temp)
                                            elif k == "checking_account_number":
                                                to_sub_account = int(v)
                                                d_temp["to_sub_account"] = to_sub_account  # add to transaction log
                                                flag_transfer_sub_type = True  # update confirmation flag
                                                d_temp["flag_transfer_sub_account"] = flag_transfer_sub_type  # update for transation log
                                                print("3:", d_temp)
                                                #return d_temp

                            elif to_sub_account_type == "saving":
                                for keys, values in self.account_details1.items():  # look into dictionary to validate accounts
                                    if keys == str(to_account):  # look for the to_account ot be valid or not
                                        flag_transfer_account = True  # if found, it's valid
                                        print(flag_transfer_account)
                                        msg = "Transfer account confirmed."  # message for transaction log
                                        d_temp["transfer_account_message"] = msg  # update for transcation log
                                        for k, v, in values.items():  # look in sub dictionary for sub account type
                                            if k == "saving_account_number":  # look if sub account type is valid
                                                flag_transfer_sub_type = True  # if found it's valid
                                                msg = "Transfer account sub type confirmed"  # message for transaction log
                                                d_temp["transfer_sub_type_message"] = msg  # update for transation log
                                                d_temp["flag_transfer_sub_account"] = flag_transfer_sub_type # update for transation log
                                            elif k == "saving_account_number":
                                                to_sub_account = int(v)
                                                d_temp["to_sub_account"] = to_sub_account  # add to transaction log
                                                flag_transfer_sub_type = True  # update confirmation flag
                                                d_temp["flag_transfer_sub_account"] = flag_transfer_sub_type  # update for transation log
                                                print("4:", d_temp)
                                                #return d_temp
                            try:
                                if flag_transfer_account != True or flag_transfer_sub_type != True:
                                    raise TypeError
                            except TypeError:
                                msg = "Error 127: Either the transfer destination account or the sub account could not be confirmed. "
                                d_temp["transfer_account_message"] = msg  # update for transcation log
                                print("5:", d_temp)
                                return d_temp

                            else:
                                if flag_transfer_account == True and flag_transfer_sub_type == True:
                                    flag_valid_transfer = True
                                    d_temp["check_transfer_flag"] = flag_valid_transfer   # update to transaction log
                                    print("6:", d_temp)
                                    return d_temp


    def transfer_deposit(self, kwargs_1, kwargs_2): #method to deposit the transfered amount to the desintation account
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1

        # local variables
        d_temp = {}  # placeholder for transaction log from transfer deposit
        msg = ""  # placholder for message for transaction log
        to_sub_acct_bal = 0  # temp variable for collecting begining account balance of destination account
        temp_bal = 0  # temp variable for calculated balance after transfer deposit
        to_final_balance = 0  # temp variable to hold the final account balance

        try: #collect from method input

            d_in_check_funds = kwargs_1
            print(d_in_check_funds)
            d_in_check_transfer = kwargs_2
            print(d_in_check_transfer)
            tran_amount = float(d_in_check_funds["tran_amount"])
            print(tran_amount)
            flag_funds = d_in_check_funds["flag_sufficient_funds"]
            print(flag_funds)
            to_account = d_in_check_transfer["transfer_to_account"]
            print(to_account)
            print(type(to_account))
            to_sub_account_type = d_in_check_transfer["to_sub_account_type"]
            print(to_sub_account_type)
            flag_transfer = d_in_check_transfer["check_transfer_flag"]
            print(flag_transfer)


        except KeyError:
            msg = "Error 128: Issue with transaction data, transfer deposit not competed."
            d_temp["transfer_deposit_message"] = msg
            return d_temp

        else:

            try: #if the funds were found to be insufficient - no deposit to be made
                if flag_funds != True:
                    raise TypeError
                elif flag_transfer != True:
                    raise TypeError

            except TypeError: #method action for insufficient funds
                msg = "Error 129: Insufficient funds or invalid destination account. Transfer deposit not completed"
                d_temp["transfer_deposit_message"] = msg
                print(d_temp)
                return d_temp

            else: #the funds were sufficient and the transfer account was valid, proceed with deposit

                if to_sub_account_type == "checking":
                    for keys, values in self.account_details1.items():
                        if keys == str(to_account):
                            for k, v in values.items():
                                if k == "checking_balance":
                                    sub_acct_bal = float(v)
                                    d_temp["to_account_balance_beg"] = v
                                    temp_bal = sub_acct_bal + tran_amount
                                    self.account_details1[str(to_account)]["checking_balance"] = str(temp_bal)
                                    final_balance = self.account_details1[str(to_account)]["checking_balance"]
                                    d_temp["to_account_balance_end"] = final_balance
                                    msg = "Transfer deposit successful."
                                    d_temp["transfer_deposit_message"] = msg
                                    print(d_temp)
                                    return d_temp
                if to_sub_account_type == "saving":
                    print(to_sub_account_type)
                    for keys, values in self.account_details1.items():
                        if keys == str(to_account):
                            for k, v in values.items():
                                if k == "saving_balance":
                                    sub_acct_bal = float(v)
                                    d_temp["to_account_balance_beg"] = v
                                    temp_bal = sub_acct_bal + tran_amount
                                    self.account_details1[str(to_account)]["saving_balance"] = str(temp_bal)
                                    final_balance = self.account_details1[str(to_account)]["saving_balance"]
                                    d_temp["to_account_balance_end"] = final_balance
                                    msg = "Transfer deposit successful."
                                    d_temp["transfer_deposit_message"] = msg
                                    print(d_temp)
                                    return d_temp


    def transfer_withdraw(self, args, kwargs_1, kwargs_2):  # method to actually take funds from client account
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1

        # local variables
        sub_acct_bal = 0  # variable to capture temporary starting balance of account
        temp_bal = 0  # variable to capture temporary calculated ending balance of account
        final_balance = 0  # variable to capture the final balance
        d_temp = {}
        msg = ""

        try:  # collect data from method input
            account = args
            print(account)
            d_check_funds = kwargs_1
            print(d_check_funds)
            d_in_check_transfer = kwargs_2
            print(d_in_check_transfer)
            sub_account_type = d_check_funds["sub_account_type"]
            print(sub_account_type)
            flag_funds = d_check_funds["flag_sufficient_funds"]
            print(flag_funds)
            tran_amount = float(d_check_funds["tran_amount"])
            print(tran_amount)
            flag_transfer = d_in_check_transfer["check_transfer_flag"]
            print(flag_transfer)

        except KeyError:  # if method input data incomplete, error message and leave method
            msg = "Error 130: Issue with transaction data, withdrawal transaction not completed."
            d_temp["transfer_withdraw_message"] = msg
            print(d_temp)
            return d_temp

        else:  # if input data found, proceed with method

            try:
                if flag_funds != True or flag_transfer != True:
                    raise TypeError

            except TypeError:
                msg = "Error 131: Insufficient funds or invalid transfer destination account, no withdrawal transaction processed."
                d_temp["transfer_withdraw_message"] = msg
                print(d_temp)
                return d_temp

            else:
                if flag_funds == True and sub_account_type == "checking":
                    for keys, values in self.account_details1.items():  # look into account details
                        if keys == str(account):
                            for k, v, in values.items():
                                if k == "checking_balance":  # if the account matches the provided client sub account
                                    sub_acct_bal = float(v)
                                    d_temp["transfer_withdraw_begin_balance"] = v
                                    temp_bal = sub_acct_bal - tran_amount
                                    self.account_details1[str(account)]["checking_balance"] = str(temp_bal)
                                    final_balance = self.account_details1[str(account)]["checking_balance"]
                                    d_temp["transfer_withdraw_end_balance"] = final_balance
                                    msg = "Withdrawal from client account complete."
                                    d_temp["transfer_withdraw_message"] = msg
                                    print(d_temp)
                                    return d_temp
                elif flag_funds == True and sub_account_type == "saving":
                    for keys, values in self.account_details1.items():  # look into account details
                        if keys == str(account):
                            for k, v, in values.items():
                                if k == "saving_balance":  # if the account matches the provided client sub account
                                    sub_acct_bal = float(v)
                                    d_temp["transfer_withdraw_begin_balance"] = v
                                    temp_bal = sub_acct_bal - tran_amount
                                    self.account_details1[str(account)]["saving_balance"] = str(temp_bal)
                                    final_balance = self.account_details1[str(account)]["saving_balance"]
                                    d_temp["transfer_withdraw_end_balance"] = final_balance
                                    msg = "Withdrawal from client account complete."
                                    d_temp["transfer_withdraw_message"] = msg
                                    print(d_temp)
                                    return d_temp


    def check_balance(self, args): #method for allowing client ot check their balances
        self.__init__(self)
        #self.tran_history
        #self.account_details
        #self.account_details1

        #local variables
        d_temp = {}  # placeholder for account balance information
        msg = ""
        check_sub_account = 0
        savings_sub_account = 0

        try:
            account = args #collect account number
            print(account)

        except ValueError:
            msg = "Error 132: Unable to process account information, balances not provided."
            d_temp["check_balance_message"] = msg
            return d_temp

        else:

            msg = "Account Information Accessed."
            d_temp["check_balance_message"] = msg

            try:
                check_sub_account = self.account_details1[str(account)]["checking_account_number"]  #collect sub account number

            except ValueError:
                msg = "Error 133: Unable to process checking account, account may not exist."
                d_temp["checking_balance_message"] = msg


            else:
                msg = "Checking account confirmed."
                d_temp["checking_balance_message"] = msg

                try:
                    d_temp["checking_balance_amount"] = self.account_details1[str(account)]["checking_balance"]  # create key:value, store balance, for results

                except ValueError:
                    msg = "Error 134: Error in retrieving account balance for checking account. Please see Teller."
                    d_temp["checking_balance_amount"] = None
                    d_temp["checking_balance_message"] = msg

                else:
                    try:
                        savings_sub_account = self.account_details1[str(account)]["saving_account_number"]  # collect sub account number

                    except ValueError:
                        msg = "Error 135: Unable to process savings account, account may not exist."
                        d_temp["saving_balance_message"] = msg

                    else:
                        msg = "Savings account confirmed."
                        d_temp["saving_balance_message"] = msg

                        try:
                            d_temp["saving_balance_amount"] = self.account_details1[str(account)]["saving_balance"]  # create key:value, store balance, for results

                        except ValueError:
                            msg = "Error 136: Error in retrieving account balance for savings account. Please see Teller."
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
            print("Error 137: Apologies but we cannot complete your desired transactions.")
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
            print("Error 138: Invalid credentials.")
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
        print(confirm_login)
        flag_user = confirm_login["flag_user"]
        flag_password = confirm_login["flag_password"]
        try:
            if flag_user != True or flag_password != True:
                raise TypeError

        except TypeError:
            print("Error 140: Invalid credentials.")
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