"""
main function

"""

def hello():
    print("hello")

def main ():
    hello()

#the if __xyz__ == __main__ needs this for the operatin system for custom package
# the use of underscore the convention of referring to functions
# this means if the __function__ is the __main__ function, then execute this thing
if __name__ == "__main__": #if you find the name in main
    main() #go ahead and run the main function
    #could have more functions here if you wanted



#   pass #pass means don't do anything, empty block of code, allows you to create a function but you can leave it without executing

