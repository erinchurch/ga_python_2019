x = float
s = ""

def defineAVariable ():
#    s = "i know i can figure this out, eventually."
    x = 1.1
    print("for testing purposes, defineAVariable is:\t", x)
#    print("for testing purposes, defineAVariable is:\t", s)
    return s, x


def useTheVariable (x):
    defineAVariable()
 #   print("for testing purposes, use the variable of s is:\t", s)
    print("for testing purposes, useTheVariable of x is:\t", x)

#defineAVariable()
#useTheVariable(s, x)


def main():
    x = defineAVariable()
    useTheVariable(x)

main ()

