#finish building exercise_1 python

"""


think about capital one

create an account
have minimum balance 100


check if accounts exist (ssn, account number)
confirm account
transfer money between one account to another

2 people have transaction
1 withdrawals
2 the other deposit

1 person goes shopping
takes out all her money
then over spends, has fee of $20

need to see all the transaction history
"""

#bank will have a collection of accounts with clients, some is the banks information some is the clients information
#clients will have their own accounts, some of it is their inforamtion,
#bank allows deposits, withdrawals, transfers, check balances
# user can check their balance, withdrawal, withdrawal for transfer, deposit



class Bank:

    def __init__(self):
        self.client = {

            101: {
                name: "Andrew",
                account_balance: 5000.0,
                pin: 1234,
            },
            102: {
                name: "Ethan",
                account_balance: 10000.0,
                pin: 4321,
            }

        }

        self.client_transaction_history = {

            101: {
                deposit_0: 5000.0


            },

            102: {
                deposit_0: 10000.0

            },

        }
        pass

def main(self):
    erin = Bank()
    print(self.client.items())

if __name__ == "__main__":
    erin = Bank()
    main(erin)