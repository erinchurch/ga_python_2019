"""

Write a program which will find all such numbers which are divisible by
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
#set lower bound
# create list for the results to be captured in
# for a number between the bounds
#if the number is divided by the divisible with no remainder and is not a multiple of muliplier
# then add the number to the list of numbers
# then increment the number to the next integer
#print the results


def  main():
    x = 2000
    seven_not_five_divisible(x)
    return x


def seven_not_five_divisible(x):
    n = x
    results = []
    while n < 3200:
        if n % 7 and n % 5 != 0:
            results.append(n)
        n += 1
    print(results)
    return results

if __name__ == "__main__":
    main()

