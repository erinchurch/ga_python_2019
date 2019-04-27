import datetime

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
        print("header file unavailable.")

    try:

        for line in data_file:
            field = line.split(";")
            field.pop()
            for i in range(len(field)):
                d_t = {}
                g[header[i]]=field[i]
                d_t.update(g)
                d_temp[field[0]]=d_t
                d_input.update(d_temp)

    except IOError:
        print("account detail file unavailable.")

    finally:
        header_file.close()
        data_file.close()
    return(d_input)



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
        print("client authentication file unavailable.")

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
            d_temp[field[1]] = field[2]
            d[field[0]] = d_temp
            d_input.update(d)
    except IOError:
        print("client authentication file unavailable.")

    finally:
        firm_file.close()
        return d_input


def update_transaction_history_file(fname, *args):
    tran_hist = open(fname, "a+")

    try:
        for arg in args:
           print(arg)
           now = datetime.datetime.now()
           timestamp = datetime.datetime.timestamp(now)
           t = str(timestamp)+str(arg)
           tran_hist.write(t+'\n')
    except IOError:
        print("transaction history file not found.")

    finally:
#        for lines in tran_hist: #developer check
#            print(lines) #developer check
        tran_hist.close()






if __name__ == "__main__":
#    read_account_file("accounts.txt", "headers_accounts.txt")
#    read_client_authentication_file("client_authentication.txt")
#    read_firm_authentication_file("firm_authentication.txt")
    f = str([(8, {'check_user_message': 'User name confirmed.', 'flag_user': True, 'check_password_message': 'User password validated', 'flag_password': True, 'client_account': 101}), (8.1, 'T'), (8.2, {'tran_amount': 450.0, 'sub_account_type': 'checking', 'sub_account': 501, 'sub_account_balance_begin': 4500.0, 'check_funds_message': 'Sufficient funds available in client account to complete client transaction, proceed execute transaction.', 'flag_sufficient_funds': True}), (8.3, {'transfer_to_account': 102, 'to_sub_account_type': None, 'transfer_account_message': 'Provided transfer destination account type cannot be processed'}), (8.4, {'transfer_withdraw_message': 'Issue with transaction data, withdrawal transaction not completed.'}), (8.5, {'transfer_deposit_message': 'Issue with transaction data, transfer deposit not competed.'})])
    g = str([(8, {'check_user_message': 'User name confirmed.', 'flag_user': True, 'check_password_message': 'User password validated', 'flag_password': True, 'client_account': 101})])
    h = str([(8.1, 'T')])
    i = str([(8.2, {'tran_amount': 450.0, 'sub_account_type': 'checking', 'sub_account': 501, 'sub_account_balance_begin': 4500.0, 'check_funds_message': 'Sufficient funds available in client account to complete client transaction, proceed execute transaction.', 'flag_sufficient_funds': True})])
    j = str([(8.3, {'transfer_to_account': 102, 'to_sub_account_type': None, 'transfer_account_message': 'Provided transfer destination account type cannot be processed'})])
    k = str([(8.4, {'transfer_withdraw_message': 'Issue with transaction data, withdrawal transaction not completed.'})])
    l = str([(8.5, {'transfer_deposit_message': 'Issue with transaction data, transfer deposit not competed.'})])
    update_transaction_history_file("transaction_history.txt", g, h, i, j, k, l)
