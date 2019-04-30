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

self.tran_history[5.1] = user
self.tran_history[5.2] = tran
self.tran_history[5.3] = t

self.tran_history[4.1] = user  #append transaction history to main transaction history dictionrary
self.tran_history[4.2] = tran  #append transaction history to main transaction history dictionrary
self.tran_history[4.3] = t  #update transaction history with contents of checking account balances

self.tran_history[6] = user  # append transaction history to main transaction history dictionary
self.tran_history[6.1]= tran  # append transaction history to main transaction history dictionary
self.tran_history[6.2] = s  # append transaction history to main transaction history dictionary
self.tran_history[6.3]= t # append transaction history to main transaction history dictionary

self.tran_history[8.1] = user  # append transaction history to main transaction history dictionary
self.tran_history[8.2]= tran  # append transaction history to main transaction history dictionary
self.tran_history[8.3] = s  # append transaction history to main transaction history dictionary
# self.tran_history[8.4]= u # append transaction history to main transaction history dictionary
self.tran_history[8.5] = t  # append transaction history to main transaction history dictionary
self.tran_history[8.6] = v  # append transaction history to main transaction history dictionary

