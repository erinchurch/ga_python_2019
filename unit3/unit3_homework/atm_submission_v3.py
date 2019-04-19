class ConfirmClient:
    accounts = {
        101: {"pin": 1234,},
        102: {"pin": 2345,},
        103: {"pin": 3456, },
    }
    def check_account(self, c):
        self.accounts
        account_confirm = bool
        for keys, values in self.accounts.items():
            if keys == c:
                account_confirm = True
#                print(account_confirm)
#        print("checking confirm account class level dictionary.\t", self.accounts.items())
        return account_confirm

    def check_pin(self, c, p):
        self.accounts
        pin_confirm = bool
        for keys, values in self.accounts.items():
            if keys == c:
                for k, v in values.items():
                    if k == "pin":
                        if v == p:
                            pin_confirm = True
#                            print(pin_confirm)
#        print("checking confirm pin class level dictionary.\t", self.accounts.items())
        return pin_confirm

class ServiceSelection:

    def transaction_type(self):
        tran_type = ""
        print("Please select from the following options:\t")
        print('"C" for Check Balance of your accounts.')
        print('"D" for Deposit funds.')
        print('"W" for Withdrawal funds.')
        print('"T" for Transfer funds.')
        tran_type = input("Please make your selection.\t")
        print("You selected:\t", tran_type)
        return tran_type

class Transactions:

    account_details = {
        101: {"checking": 501,
              501: 4500.0,
              "savings": 601,
              601: 5000.0,
              "name": "Erin Church",
              },
        102: {"checking": 502,
              502: 3500.0,
              "savings": 602,
              602: 12000.0,
              "name": "Ronald Williams",
              },
        103: {"checking": 503,
              503: 1200.0,
              "savings": 603,
              603: 2300.0,
              "name": "Dirk Church",
              },
    }
    tran_history = {
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
        if tran == "D":
            t = Transactions.deposit_funds(self, c)
            print("You have deposit and new account balance:\t", t)
        elif tran == "C":
            t = Transactions.check_balance(self, c)
            print("You would like to check your balances.\t", t)
        elif tran == "W":
            s = Transactions.check_funds(self,c)
            print(s)
            t = Transactions.withdraw_funds(self,c, s[0], s[1], s[2], s[3])
            print("Your withdrawal and new account balance:\t",t)
        elif tran == "T":
            s = Transactions.check_funds(self,c)
            print("results, check funds.\t", s)
            u = Transactions.transfer_account(self, c, s[3])
            print("results, transfer account validation.\t", u)
            t = Transactions.withdraw_funds(self, c, s[0], s[1], s[2], s[3])
            print("results withdraw funds:\t", t)
            v = Transactions.transfer_deposit(self, c, s[0], u[0], u[1], u[2], u[3])



    def check_funds(self,c):
        self.account_details
        self.tran_history
        tran_amount = float(input("Please enter the amount you with to withdraw.\t"))
        sub_acct_type = input("Withdraw from checkings or savings account? (Type checking or saving)")
        sub_acct = 0
        sub_acct_bal = 0
        flag_sufficient_funds = bool
        for keys, values in self.account_details.items():
            if keys == c:
                for k, v in values.items():
                    if k == sub_acct_type:
                        sub_acct = v
                    elif k == sub_acct_type:
                        sub_acct = v
                    elif k == sub_acct:
                        sub_acct_bal = v
                        if sub_acct_bal >= tran_amount:
                            flag_sufficient_funds = True
                        else:
                            print("Insufficient funds.\t")
        print(sub_acct_type, sub_acct, flag_sufficient_funds)
        return tran_amount, sub_acct_type, sub_acct, flag_sufficient_funds

    def withdraw_funds(self,c, tran_amount, sub_account_type, sub_account, flag_sufficient_funds):
        self.account_details
        self.tran_history
        d_sub_temp = {"tran_type":"withdrawal",}
        d_sub_temp["account"] = c
        d_sub_temp["sub_account_type"]=sub_account_type
        sub_acct_bal = 0
        temp_bal = 0
        if flag_sufficient_funds == True:
            for keys, values in self.account_details.items():
                if keys == c:
                    for k, v in values.items():
                        if k == sub_account:
                            sub_acct_bal = v
                            d_sub_temp["sub_account_balance_begin"] = v
                            temp_bal = v - tran_amount
                            self.account_details[c][k] = temp_bal
                            d_sub_temp["transaction_amount"] = tran_amount
                            d_sub_temp["sub_account_balance_end"] = temp_bal
                            print(self.account_details[c][k])
        self.tran_history[6] = d_sub_temp
        print(self.tran_history[6])
        print(self.account_details[c][sub_account])
        return tran_amount, temp_bal

    def transfer_account(self,c, flag_sufficient_funds):
        self.account_details
        to_account = 0
        to_sub_account_type = ""
        to_sub_account = 0
        flag_transfer_account_valid = bool
        if flag_sufficient_funds == True:
            to_account = int(input("Please provide the account number to receive your transfer.\t"))
            to_sub_account_type = input("Is it a checkings or savings account? Type checking or saving.\t")
            for keys, values in self.account_details.items():
                if keys == to_account:
                    for k, v, in values.items():
                        if k == to_sub_account_type:
                            to_sub_account = v
                            print(to_sub_account)
                            flag_transfer_account_valid = True
                            print(flag_transfer_account_valid)
                            print(to_account, to_sub_account_type, to_sub_account, flag_transfer_account_valid)
        return to_account, to_sub_account_type, to_sub_account, flag_transfer_account_valid

    def transfer_deposit(self, c, tran_amount, to_account, to_sub_account_type, to_sub_account, flag_transfer_account_valid):
        self.account_details
        self.tran_history
        d_sub_temp = {"tran_type":"withdrawal",}
        d_sub_temp["account"] = to_account
        d_sub_temp["sub_account_type"] = to_sub_account
        d_sub_temp["from_account"] = c
        d_sub_temp["sub_account_type"]= to_sub_account
        d_sub_temp["transaction_amount"] = tran_amount
        sub_acct_bal = 0
        temp_bal = 0

        if flag_transfer_account_valid == True:
            for keys, values in self.account_details.items():
                if keys == to_sub_account:
                    for k, v in values.items():
                        if k == to_sub_account:
                            sub_acct_bal = v
                            d_sub_temp["to_account_balance_begin"] = v
                            temp_bal = v + tran_amount
                            d_sub_temp["to_account_balance_end"] = temp_bal
                            self.account_details[to_account][to_sub_account] = temp_bal
                            print(self.account_details[k][v])
        self.tran_history[8]=d_sub_temp
        print(self.tran_history[8])

    def deposit_funds(self, c):
        self.account_details
        self.tran_history
        tran_amount = float(input("Please enter the amount you wish to deposit."))
        sub_acct_type = input("Deposit to checkings or savings account? (Type checking or saving)\t")
        sub_acct = 0
        sub_acct_bal = 0
        temp_bal = 0
        d_sub_temp = {"tran_type":"deposit",}
        d_sub_temp["account"] = c
        d_sub_temp["sub_account_type"]=sub_acct_type
        for keys, values in self.account_details.items():
            if keys == c:
                for k, v in values.items():
                    if k == sub_acct_type:
                        sub_acct = v
                        d_sub_temp["sub_account"] = sub_acct
                    elif k == sub_acct:
                        sub_acct_bal = v
                        temp_bal = v + tran_amount
                        d_sub_temp["sub_account_balance_begin"] = sub_acct_bal
                        self.account_details[c][k] = temp_bal
                        d_sub_temp["transaction_amount"] = tran_amount
                        d_sub_temp["sub_account_balance_end"] = temp_bal
                        print(self.account_details[c][k])
        self.tran_history[5] = d_sub_temp
        print(self.tran_history[5])
        print(self.account_details[c][sub_acct])
        return tran_amount, temp_bal

    def check_balance(self, c):
        self.tran_history
        self.account_details
        account = c
        sub_acct_1 = 0
        sub_acct_2 = 0
        sub_type_1 = ""
        sub_type_2 = ""
        d_sub_temp = {"tran_type": "check_balance",
                      "account": c, }
        for keys, values in self.account_details.items():
            if keys == c:
                for k, v in values.items():
                    if k == "checking":
                        sub_type_1 = "checking"
                        sub_acct_1 = v
                        d_sub_temp[sub_type_1] = sub_acct_1
                        print(k, v)
                    elif k == "savings":
                        sub_type_2 = "savings"
                        sub_acct_2 = v
                        d_sub_temp[sub_type_2] = sub_acct_2
                        print(k, v)
                    elif k == sub_acct_1:
                        d_sub_temp[sub_acct_1] = v
                        print(k, v)
                    elif k == sub_acct_2:
                        d_sub_temp[sub_acct_2] = v
                        print(k, v)
        self.tran_history[4] = d_sub_temp
        print(self.tran_history[4])


def main():
    a = ConfirmClient
    c = int(input("Please provide your card number.\t"))
#    flag_account_confirm = ConfirmClient.check_account(a, c)
#    p = int(input("Please enter your pin number.\t"))
#    flag_pin_confirm = ConfirmClient.check_pin(a, c, p)
#    if flag_account_confirm == True and flag_pin_confirm == True:
#        print("Account confirmed.\t")
#    else:
#        print("Apologies, we cannot confirm your account.\n")
#        print("Please see a teller.\t")
    b = ServiceSelection
    tran = ServiceSelection.transaction_type(b)
    print("check outside class", tran, c)
    d = Transactions
    e = Transactions.Transaction_Calls(d, tran, c)

main()

"""
a = ConfirmClient
c = int(input("Please provide your card number.\t"))
flag_account_confirm = ConfirmClient.check_account(a,c)
p = int(input("Please enter your pin number.\t"))
flag_pin_confirm = ConfirmClient.check_pin(a, p)
"""