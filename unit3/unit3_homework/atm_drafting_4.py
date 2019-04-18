#figure out how to add the transaction log for each transaction type
#oustanding: deposit, withdrawal, transfer

#to do: nest them in classes, methods, write main function to call it all

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
#accepts users withdrawal amount
#subtracts withdrawal from balance
#place holder for actual transaction
#prints remaining balances, leaves

#transfer method
#ask from-to checking versus savings
#prints balances available
#accepts user transfer amount
#subtract from one account, add to the other
#prints new balances, leaves


#user_name = ""
#savings_account = int
#checking_account = int
#savings_balance = float
#checking_balance = float
#pin = int


client_dict = { #created in advance testing account dictionary
             101:
                 {
                 "user_name": "Erin Church",
                 "savings_account": 501,
                 "checking_account": 601,
                 501:5000.00,
                 601: 6000.00,
#                 "savings_balance": 5000.0,
#                 "checking_balance": 6000.0,
                 "pin": 1234
                 },

            102:
                {
                "user_name": "Ronald Williams",
                "savings_account": 502,
                "checking_account": 602,
                502: 4500.0,
                602: 5500.0,
                "pin": 4321,
                },

        }


dict_tran = { #for testing, transaction dictionary
            0: {
                "tran_type": "",
                "client_account": "",
                "sub_account_type": "",
                "sub_account": "",
                "start_balance": "",
                "transaction_amount": "",
                "from_client_account": "",
                "to_client_account": "",
                "from_sub_account": "",
                "to_sub_account": "",
                "from_transaction_amount": "",
                "to_transaction_amount": "",
                "from_start_balance": "",
                "to_start_balance": "",
                "from_end_balance": "",
                "to_end_balance": "",
            },

            1: {
                "tran_type": "daily_balance",
                "client_account":101,
                "sub_account_type": "checking_account",
                "sub_account":601,
                "start_balance":6000.0,
            },
            2: {
                "tran_type": "daily_balance",
                "client_account": 102,
                "sub_account_type": "savings_account",
                "sub_account": 501,
                "start_balance": 5000.0,
            },
        3: {
            "tran_type": "daily_balance",
            "client_account": 102,
            "sub_account_type": "savings_account",
            "sub_account": 502,
            "start_balance": 4500.0,

        },
        4: {
            "tran_type": "daily_balance",
            "client_account": 102,
            "sub_account_type": "checking_account",
            "sub_account": 602,
            "start_balance": 5500.0,
        },

}



print("Accessing parent client dictionary:\t", client_dict.items()) #developer check, make sure there is nothing wrong with parent account dictionary
print("Accessing parent transaction dictionary:\t", dict_tran.items()) #developer check, make sure there is nothing wrong with the parent transaction dictionary


"""
#may fix later, may delete
#get new account number
new_account = 0
last_account = 0
for keys, values in client_dict.items():
    print(keys)
    last_account = keys
    print(last_account)
print("out of loop:\t", last_account)
new_account += last_account
print(new_account)
"""
#add a new account
temp_dict_new_account = {"user_name":"Dirk Church",
             "checking_account": 702,
             702: 3000.0,
             "pin": 1122,}

client_dict[103]=temp_dict_new_account #SUCCESSFULLY ADDED NEW DICTIONARY SET
print("Accessing parent dictionary, new account:\t", client_dict.items())

#get the last number used in the transaction dictionary
counter_trans = 1
for keys, values in dict_tran.items():
#    print(keys) #developer check
    counter_trans +=1 #create a new transaction number, greater than any other in the dictionary
#    print(counter_trans) #developer check
temp_dict_new_account_tran = {
            "tran_type": "test_new_account",
            "client_account": 103,
            "sub_account_type": "savings_account",
            "sub_account": 702,
            "start_balance": 3000.0,
}
dict_tran[counter_trans] = temp_dict_new_account_tran #add new transaction

#print("Accesing parent transaction dictionary, new transaction:\t", dict_tran.items()) #developer check of new transaction



#depositing funds
#to do, add check identify
#to do, add transaction history update
select = "checking_balance"

for keys , values in client_dict.items(): #SUCCESSFULLY UPDATED A SUB DICTIONARY KEY'S VALUE
    if keys == 103:
        for k, v in values.items():
            if k == select:
                print("before deposit\t", v)
                client_dict[103][select] += 1000
                print("after deposit\t", client_dict[103][select])

print("Accessing parent dictionary, deposit confirmation:\t", client_dict.items())

#withdrawl funds
# to do, add transaction history update

d_w_subtran_temp = {"tran_type": "",
                "client_account": "",
                "sub_account_type": "",
                "sub_account": "",
                "start_balance": "",
                "transaction_amount": "",
                "from_transaction_amount": "",
                "from_start_balance": "",
                "from_end_balance": "",}
account_confirm = bool #account confirmation flag
pin_confirm = bool #pin confirmation flag
d_w_subtran_temp["tran_type"] = "w" #set transaction type
x = "checking_account" #account type
c = 101 #account number
d_w_subtran_temp["client_account"] = c #set transaction history client account number
p = 1234 #pin number
w = 500.0 #withdrawl amount
d_w_subtran_temp["transaction_amount"] = w #set transaction history client account number
s = "" #sub account number
b=0 #balance after withdrawal


d_w_subtran_temp["start_balance"] = 4500.0
print(d_w_subtran_temp)
#check identity
for keys, values in client_dict.items():
    if keys == c:
        account_confirm = True
        for k, v in values.items():
            if k == "pin" and v == p:
                pin_confirm = True
                print(account_confirm, pin_confirm) #developer test
#get savings account number
if account_confirm == True and pin_confirm == True: #do nothing unless the identity is confirmed
    for keys, values in client_dict.items(): #look in parent dictionary
        if keys == c: #for the dictionary record equal to the account
            for k, v in values.items(): #for the sub dictionary
                if k == x: #if they key equals the account type requested
                    d_w_subtran_temp["sub_account_type"] = x
                    s = v #set temp variable equal to sub account number in question
                    print(s) #developer check
#print(s)

#make withdrawal
if account_confirm == True and pin_confirm == True:  # do nothing unless the identity is confirmed
    for keys, values in client_dict.items():  # look in parent dictionary
        if keys == c: #for the dictionary record equal to the account
            for k, v in values.items(): #look in sub dictionary
                if k == str(s): #match to the sub-account selected
                    print(v) #check values before operation
                    d_w_subtran_temp["start_balance"] = v
                    d_w_subtran_temp["from_start_balance"] = v
                    d_w_subtran_temp["from_transaction_amount"] = -w
                    b=v-w #calculation of new balance
                    print(b) #developer check
                    client_dict[c][s]=b #update dictionary value
                    print(client_dict[c][s]) #developer check that values was updated
                    d_w_subtran_temp["from_end_balance"] = client_dict[c][s]

#to do: the full transaction history isn't working, e.g. from_end_balance

print("temp tran history:\t", d_w_subtran_temp)

counter_trans = 1
for keys, values in dict_tran.items():
#    print(keys) #developer check
    counter_trans +=1 #create a new transaction number, greater than any other in the dictionary
#    print(counter_trans) #developer check
dict_tran[counter_trans] = d_w_subtran_temp #add new transaction for withdrawal
print("update to tran history.\t", dict_tran.items())


#client_dict[101][str(s)]=b
#print("oustide test", client_dict[101][str(s)])


#Transfer
#to do, add transaction history functionality

from_c = 101 #from account
to_c = 102 #to account
from_x = "checking_account" #from type
to_x = "checking_account" #to type
t = 500.00 #transfer amount
from_s = "" #sub account number from
to_s = "" #sub account number to
from_b = 0 #calculation balance from
to_b = 0 #calcuation balance to

if account_confirm == True and pin_confirm == True: #get sub account number
    for keys, values in client_dict.items():
        if keys == from_c:
            for k, v, in values.items():
                if k == from_x:
                    from_s = v  #get sub account number
                    print(v, from_s) #developer check

if account_confirm == True and pin_confirm == True: #withdraw amount from, from account
    for keys, values in client_dict.items():
        if keys == from_c:
            for k, v in values.items():
                if k == str(from_s):
                    print(v) #developer check
                    from_b = v - t  #calculate new balance after withdrawal
                    client_dict[from_c][from_s]=from_b #update dictionary #later can remove the string convert
                    print(client_dict[c][from_s]) #developer check

#transation as the Bank, deposit the transfer amount to the other account

for keys, values in client_dict.items(): #get sub account number
    if keys == to_c:
        for k, v, in values.items():
            if k == str(to_x): #edit dictionary to store it as a int instead fo a string
                print(v)
                to_s = v #set temp account equal to the sub account
                print(to_s)

#transation as the Bank, deposit the transfer amount to the other account
for keys, values in client_dict.items():
    if keys == to_c:
        for k, v in values.items():
            if k == to_s: #sub account number, collect the current balance
                print(v) #developer check
                to_b = v + t #calc temporary balance to post deposit balance
                print(to_b) #developer check
                client_dict[to_c][to_s] = to_b #update dictionary
                print(client_dict[to_c][to_s]) #developer check on dictionary


#I don't remember what this is for may fix, may delete
"""

for keys, values in client_dict.items():
    for key, value in values.items():
        print("Accessing subdictionary:\t", key, value)

erin = 101 #test values account
erin_pin = 1234 #test values pin
account_confirm = bool #creating confirmation variables
pin_confirm = bool #creating confirmation variables


for keys, values in client_dict.items(): #practice confirming the account
    if keys == erin:
        account_confirm = True
        print("Account confirmation:\t", account_confirm)
#    else:
#        print("wrong key")

for keys, values in client_dict.items(): #practice confirming the pin
    for key, value in values.items():
        if key == "pin" and value == erin_pin:
            pin_confirm = True
            print("Pin Confirmation:\t", pin_confirm)
#        else:
#            print("failed pin confirmation logic.\t")

choice = "deposit"
account_type = "savings_account"
account_selected = ""
amount = 5000
new_balance = 0

if account_confirm == True and pin_confirm == True:
    for keys, values in client_dict.items():
        if keys == erin:
            for key, value in values.items():
                if key == account_type:
                    account_selected = str(value)
                    print("account number for", account_type, account_selected, value) #developer test of loop
                    print(type(account_selected), account_selected) #develop test of look up for temporary variable

if account_confirm == True and pin_confirm == True:
    for keys, values in client_dict.items():
        if keys == erin:
            for key, value in values.items():
                if key == account_selected:
                    print("before deposit:\t", value)
                    value += amount #only temporary update
#                    erin["501"] = value #doesn't work
                    print("after deposit:\t", value)



for keys, values in client_dict.items():
    for key, value in values.items():
        print("checking for update in subdictionary:\t", key, value)
"""