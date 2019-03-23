"""
explain:
This is a compound interest calculator that can be used for investments or it can be used for amortizing loans, such as a mortgage.

to do: correct data types, if what is given incorrect.
be able to convert currencies
be able to receive input from files or other sources, instead of users.
"""


accrued_amount = float # create variable for accrued amount, float

principal_amount = float # create variable for princiipal values, cannot be null, float
interest_rate = float # create varaible for interest rate, annual, float
time_in_years = float # create variable for time period, in years, float
number_payments_per_year = float # create variable for compound frequency, float

# ask for the principal amount

principal_amount = float(input("Please provide the total principal amount, e.g. $10,000.00 as 10000.\t"))

# ask for the interest rate in decimals or convert to decimals

interest_rate = float(input ("Please provide your interest rate in decimals, e.g. 10% interest is 0.10.\t"))

# ask for the the length fo the investment or time period in years.

time_in_years = float(input ("Please input the length of time, in years.\t"))

# ask for the value of compounding frequency, time per year

number_payments_per_year = float(input ("Please input the number of payments or compound periods per year.\t"))


# Calculate the acrrued amount

accrued_amount = principal_amount * ((1 + (interest_rate / number_payments_per_year))**(time_in_years * number_payments_per_year))

# PRINT USER PROVIDED VALUE FOR principal_amount
print("For a principal amount of $", principal_amount)
# PRINT USER PROVIDED VALUE FOR interest_rate
print("For an annual interest rate of ", interest_rate)
# PRINT USER PROVIDED VALUE FOR time_in_years
print("For an investment period of ", time_in_years)
# PRINT USER PROVIDED VALUE FOR number_payments_per_year
print("For a payment frequency per year of ", number_payments_per_year)
# PRINT ACCRUED AMOUNT, ROUNDED WITH DOLLAR SIGN
print("Your total Accrued Amount would be $", round(accrued_amount, 2))


#sSURESH COMMENTS - DON'T USE TEMPORARY VARIABLES, THEY BURN MEMORY
#class suggested i not use caps lock