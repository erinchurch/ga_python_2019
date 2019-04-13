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
        client = {

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

        client_transaction_history = {

            101: {
                deposit_0: 5000.0


            },

            102: {
                deposit_0: 10000.0

            },

        }
        pass

    def check_client(self): #check account exits
        #confirm pin
        #account access allowed
        pass

    def create_new_client(self):
        pass

    def check_balance(self):
        #check if client confirmed, via check_client
        #get account number
        #look up client account_balance
        #give account balance to whatever needed
        pass

    def money_out(self):
        #check if client confirmed, via check client
        #ask how much to take out
        #check balance relative money out
        # if money out is less than balance,
        #confirm withdrawal (message to user)
        #sub tract money out from balance, update balance
        #record transaction in log
        pass

    def money_in(self):
        #check if client confirmed, via check client
        #ask how much to deposit
        #confirm deposit (message to user)
        #add money in to balance, update balance
        #record transaction in log
        pass

    def money_out_transfer(self):
        #check if client confirmed, via check client
        # ask how much to transfer
        #ask who to transfer to
        #find account they want to transfer to
        #check balance relative money out
        # if money out is less than balance,
        #confirm withdrawal (message to user)
        #sub tract money out from balance, update balance
        #record transaction in log
        #confirm deposit to other account
        #add money in to other balance, update other balance
        #record transaction in log for other account
        pass

    def transaction_history(self):
        #check if client confirmed via client check
        #print or return the client's transaction history

    def client_request(self):
        # ask client what they want to do
        # store that selection
        pass



class Client(bank):

    def __init__(self):
        super().__init__(self)


    def give_client_id(self):
        #user gives the account number
        #user gives the pin
        #call check client from the parent
        pass

    def withdrawal(self):
        #collect from user the amount they want to withdrawal
        #call the parents money out, giving it the request withdrawal and the confirmed
        pass

    def deposit(self):
        #collect from user how much they want to deposit in their account
        #call parents money in, giving the request deposit and the confirmed
        pass

    def transfer(self):
        #collect amount desired to transfer
        #the destination account for the transfer
        #call parent money_out_transfer
        pass

    def check_balance(self):
        #call parents check balance
        pass

    def check_history(self):
        #call parents transaction history
        #return that history for user to see
        pass

def main():
    x = Client()

if __name__ == "__main__":
    main()






