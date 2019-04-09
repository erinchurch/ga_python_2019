user_input = ""
is_palindrome = bool

def collect_user_input():
    user_input = input("Please provide the phrase, we'll check if it is a Palindrome!\t")
    print(user_input)
    return user_input

def remove_punt(user_input):
    user_input_less_punt = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    for i in range(len(user_input)):
        print(user_input[i])
        if user_input[i] in punctuations:
            user_input_less_punt += user_input_less_punt.replace(user_input[i], "")
        else:
            user_input_less_punt += user_input[i]
    print("without punct\t", user_input_less_punt)
    return user_input_less_punt

def main ():
    x = collect_user_input()
    print("X is\t", x)
    y = remove_punt(x)
    print("Y is\t", y)

if __name__ == "__main__":
    main()