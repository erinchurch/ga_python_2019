import datetime
"""
DIDNT WORK
k = datetime.datetime.now()
k.timestamp()
print(k)
print(k.timestamp())


#timestamp = datetime.date.fromtimestamp()
#print("Date =", timestamp)

def update_files(fname):
    account = '503;1200.0'
    x = len(account)
    counter = 0
    s = "checking_balance"

    tupdate = open(fname, "r+")

    for lines in tupdate:
        print(lines)
        print(type(lines))
        print(len(lines))
        for i in range(len(lines)):
            print(i)
            lines[i + len(account)]
            print(lines[i + len(account)])
            if lines[i+len(account)] == account:
                flag = True
                print(flag)
#            if lines[i+len(account)] == account:
#                counter += 1
#            print('i', i)
#            print("counter", counter)


    tupdate.close()

update_files("update.txt")"""

"""
DIDN'T WORK
s = "101;checking;501;4500.0;saving;601;5000.0;Erin Church;erinchurch;"
print(s)

s_1 = "501;4500.0"
print(len(s_1))
print(s_1)
counter = 0
s_2 = "501;5000.0"

for i in range(len(s)):
    print(i)
    print(s[i:(i+len(s_1))])
    if s[i:(i+len(s_1))] == s_1:
        counter += 1
        print("counter", counter)
        print(s)
        #s.replace(s_1, s_2)
        s[i:(i + len(s_1))].replace(s_1, s_2)
        print(s)
        
"""

"""
#WORKS!!
s = "101;checking;501;4500.0;saving;601;5000.0;Erin Church;erinchurch;"
print(s)
s_before = ""
s_after = ""
s_new = ""
s_test = ""
counter = 0
s_1 = "501;4500.0"
s_2 = "501;5000.0"
flag = len(s_1) == len(s_2)
print(flag)
s.replace(s_1, s_2)
print(s)

for i in range(len(s)):
    #print("i", i)
    #print("section", s[i:(i+len(s_1))])
    if s[i:(i+len(s_1))] == s_1:
        counter += 1
        print("counter", counter)
        s_before = s[0:(i-1)]
        print("s_before", s_before)
        s_after = s[(i+len(s_1)+1):len(s)]
        print("s_after", s_after)
        s_new = s_before + ";" + s_2 + ";" + s_after
        print("new", s_new)
        s_test = s_before + ";" + s_1 + ";" + s_after
        print("test", s_test)
        print("original", s)
        #t = s[i:(i+len(s_1))]
        #print("t", t)

if s_test == s and counter ==1:
    flag2 = True
print(flag2)
"""



s = "101;checking;501;4500.0;saving;601;5000.0;Erin Church;erinchurch;"
s_new = "101;checking;501;5000.0;saving;601;5000.0;Erin Church;erinchurch;"

"""
#doesn't work
def update_account(fname, s_old, s_new):

    update_account_file = open(fname, "r+")
    s_to_be_replaced = s_old
    print("old", s_to_be_replaced)
    s_to_be_inserted = s_new
    print("new", s_to_be_inserted)
    flag = bool
    flag2 = bool


    for lines in update_account_file:
        print(lines)
        print(type(lines))
        print(s_to_be_replaced)
        print(type(s_to_be_replaced))
        flag = lines == s_old
        print(flag)
        if lines == s_to_be_replaced:
            flag2 = True
            print(flag)
            print(lines)

    update_account_file.close()

update_account("update.txt", s, s_new)
"""

#doesn't work
def collect_update_for_file(fname, s_old_snip, s_new_snip):

    update_account_file = open(fname, "r+")

    #s = "101;checking;501;4500.0;saving;601;5000.0;Erin Church;erinchurch;"
    #print(s)
    s = ""
    s_before = ""
    s_after = ""
    s_new = ""
    #s_test = ""
    s_original = ""
    counter_match = 0
    counter_start_position = 0
    s_1 = s_old_snip
    s_2 = s_new_snip

    #flag_len = len(s_1) == len(s_2) #for try/except
    #print(flag_len) #for try/except
    #s.replace(s_1, s_2)
    #print(s)
   #s_test_1 = "\n104;checking;504;10000.0;saving;604;200.0;Anita Ghardi;anitaghardi;"
    #update_account_file.write(s_test_1)
    #s_test_2 = "\n105;checking;505;1000.0;saving;605;1200.0;Kenya Brown;kenyabrown;"
    #update_account_file.write(s_test_2)
    #write line to delete the accounts


    for lines in update_account_file:
        #print(lines)
        #print(type(lines))
        #print(len(lines))
        for line in range(len(lines)):
            #print(lines[line:(line + len(s_1))])
            if lines[line: (line+len(s_1))] == s_1:
                counter_match += 1
                print("counter", counter_match)
                counter_start_position = line
                print("counter start position", counter_start_position)
                s_before = lines[0:(line - 1)]
                print("before", s_before)
                s_after = lines[(counter_start_position+len(s_1)):len(lines)]
                print("s_after", s_after)
                s_new = ("\n"+s_before+";"+s_2+";"+s_after)
                print("new", s_new)
                s_original = lines
                print("original",s_original)
                return(s_original, s_new)

    update_account_file.close()


def update_account(fname, *args):

    update_account_file = open(fname, "r+")
    s_original = args[0]
    #print(s_original)
    s_new = args[1]
    #print(s_new)
    check_flag = bool

    for lines in update_account_file:
        if lines.strip("\n") == s_original.strip("\ns"):
            check_flag = True
            print("check flag", check_flag)

    update_account_file.close()

s_1 = "501;4500.0"
s_2 = "501;5000.0"



s_input = collect_update_for_file("update.txt", s_1, s_2)
#print("input", s_input)
c = update_account("update.txt", *s_input)








