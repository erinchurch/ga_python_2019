# figure out how to pull information from nested dictionaries
#figure out how to edit information from nested dictionaries





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


#user_name = ""
#savings_account = int
#checking_account = int
#savings_balance = float
#checking_balance = float
#pin = int


client_dict = {
             101:
                 {
                 "user_name": "Erin Church",
                 "savings_account": 501,
                 "checking_account": 601,
                 "501":5000.00,
#                 "savings_balance": 5000.0,
                 "checking_balance": 6000.0,
                 "pin": 1234
                 },

            102:
                {
                "user_name": "Ronald Williams",
                "savings_account": 502,
                "checking_account": 602,
                "savings_balance": 4500.0,
                "checking_balance": 5500.0,
                "pin": 4321
                },

        }

print("Accessing parent dictionary:\t", client_dict.items())




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


""""
results


/anaconda3/bin/python3 /Users/upstart/ga_python_2019/unit3/unit3_homework/atm_drafting_2.py
Accessing parent dictionary:	 dict_items([(101, {'user_name': 'Erin Church', 'savings_account': 501, 'checking_account': 601, '501': 5000.0, 'checking_balance': 6000.0, 'pin': 1234}), (102, {'user_name': 'Ronald Williams', 'savings_account': 502, 'checking_account': 602, 'savings_balance': 4500.0, 'checking_balance': 5500.0, 'pin': 4321})])
Accessing subdictionary:	 user_name Erin Church
Accessing subdictionary:	 savings_account 501
Accessing subdictionary:	 checking_account 601
Accessing subdictionary:	 501 5000.0
Accessing subdictionary:	 checking_balance 6000.0
Accessing subdictionary:	 pin 1234
Accessing subdictionary:	 user_name Ronald Williams
Accessing subdictionary:	 savings_account 502
Accessing subdictionary:	 checking_account 602
Accessing subdictionary:	 savings_balance 4500.0
Accessing subdictionary:	 checking_balance 5500.0
Accessing subdictionary:	 pin 4321
Account confirmation:	 True
Pin Confirmation:	 True
account number for savings_account 501 501
<class 'str'> 501
before deposit:	 5000.0
after deposit:	 10000.0
checking for update in subdictionary:	 user_name Erin Church
checking for update in subdictionary:	 savings_account 501
checking for update in subdictionary:	 checking_account 601
checking for update in subdictionary:	 501 5000.0
checking for update in subdictionary:	 checking_balance 6000.0
checking for update in subdictionary:	 pin 1234
checking for update in subdictionary:	 user_name Ronald Williams
checking for update in subdictionary:	 savings_account 502
checking for update in subdictionary:	 checking_account 602
checking for update in subdictionary:	 savings_balance 4500.0
checking for update in subdictionary:	 checking_balance 5500.0
checking for update in subdictionary:	 pin 4321

Process finished with exit code 0



"""