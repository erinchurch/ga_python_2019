#super broken

class ClientAccountConfirm:
    accounts_card: {
                    1: {"card": 101,
                        },
                    2: {"card": 102,
                        },
                    3: {"card": 103,
                        },
                    4: {"card": 104,
                        },
                    }
    print("checking the class level dictionary:", accounts_card.items())
    accounts_card_pin: {
                        1: {"card": 101,
                            "pin": 1234,
                            },
                        2: {"card": 102,
                            "pin": 2345, },
                        3: {"card": 103,
                            "pin": 3456
                            },
                        4: {"card": 104,
                            "pin": 4567,
                            },
                        }
    print("checking the class level dictionaries:", accounts_card_pin.items())

    def account_confirm(self, c, p): #confirm client actually has a valid card and account
        account_confirm = bool
        card = c
        self.accounts_card
#        for keys, values in self.accounts_card.items():
#            if keys == card:
#                account_confirm = True
#                print("testing account confirmation:\t", account_confirm)
#        else:
#            print("Apologies, we cannot find your account, please see a teller.\t")
        print("erin to write account confirm logic")
        pass

    def pin_confirm(self, c, p): #confirm the clients pin number
        self.accounts_card_pin
        pin_confirm = bool
        pin = p
        print("erin to write pin confirm logic")
        pass

class ClientSelection:

    def client_selection(self, account_confirm, pin_confirm): #request transaction type, only if account and pin confirmed
        print("Erin to write transaction type")
        choice = "test"
        return choice

    def transaction_amount(self, account_confirm, pin_confirm): #request transaction amount, only if account and pin confirmed
        print("Erin to write the request for transaction amount")
        tran_amount = 0
        return tran_amount


class Client_Transactions:

    def deposit_funds(self):
        d_temp_deposit = {}
        print("erin to write deposit logic")
        return d_temp_deposit


    def withdrawal_funds(self):
        d_temp_withdrawal = {}
        print("erin to write withdrawal logic")
        return d_temp_withdrawal

    def transfer_funds(self):
        #look up information from the dictionaries
        #call deposit_funds
        #call withdrawal_funds
        d_temp_transfer = {}
        print("erin to write transfer logic")
        return d_temp_transfer

a = ClientAccountConfirm



"""
def main ():
# don't use variable letters: c, p

    print("Welcome to the Bank of Erin!") #greeting 1
    print("We look forward to serving you!") #greeting 2
    c = input("Please provide your card number.\t")
    p = input("Please provide your pin number.\t")
    a = ClientAccountConfirm #initiate client account cofirmation
    ClientAccountConfirm.account_confirm(a, c, p) #call client account confirmation
#   b = ClientPinConfirm() #initiate client pin confirmation
#   ClientPinConfirm.pin_confirm(b) #call client pin confirmation
#   c = ClientSelection() #initiate the request of transaction service type from the client
#    d = ClientSelection.client_selection(c, a, b) #call the client selection service, store selection in d
#    e = ClientSelection.transaction_amount(c, a, b) #call transaction amount, store in e







if __name__ == "__main__":
    main()
"""