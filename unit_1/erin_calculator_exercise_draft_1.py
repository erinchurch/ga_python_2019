"""
https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php

Calculator Use
Calculate compound interest on an investment or savings. Using the compound interest formula, calculate principal plus interest or principal or rate or time. Includes compound interest formulas to find principal, interest rates or final investment value including continuous compounding A = Pe^rt.

Compound Interest Equation
A = P((1 + r/n)**nt)

Where:

A = Accrued Amount (principal + interest)
P = Principal Amount
I = Interest Amount
R = Annual Nominal Interest Rate in percent
r = Annual Nominal Interest Rate as a decimal
r = R/100
t = Time Involved in years, 0.5 years is calculated as 6 months, etc.
n = number of compounding periods per unit t; at the END of each period
Compound Interest Formulas and Calculations:
Calculate Accrued Amount (Principal + Interest)
A = P(1 + r/n)nt
Calculate Principal Amount, solve for P
P = A / (1 + r/n)nt
Calculate rate of interest in decimal, solve for r
r = n[(A/P)1/nt - 1]
Calculate rate of interest in percent
R = r * 100
Calculate time, solve for t
t = ln(A/P) / n[ln(1 + r/n)] = [ ln(A) - ln(P) ] / n[ln(1 + r/n)]

"""

#START ERIN CODE
#THE FORMULA TO CALCULATE THE TOTAL ACCRUED BALANCE, ACCORDING TO THE EQUATION IS
#ACCRUED  BALANCE EQUAL TO PRINCIPAL MULTIPLIED BY THE FACTOR
# THE FACTOR IS RAISED TO A POWER EQUAL TO TIME THE FREQUENCY OF PAYMENTS PER YEAR TIMES THE NUMBER OF YEARS
# THE FACTOR IS EQUAL TO ONE PLUS THE INTERSET RATE DIVIDED BY THE NUMBER OF PERIODS.

#CREATE VARIABLE FOR ACCRUED AMOUNT, CAN BE EMPTY, FLOAT

#CREATE VARIABLE FOR PRINCIPAL BALANCE, CAN BE EMPTY, FLOAT
#CREATE VARIABLE FOR INTEREST RATE, ANNUAL, CAN BE EMPTY, ITS FLOAT

# ASK FOR VALUE OF PRINCIPAL AMOUNT, DOLLARS
# ASK FOR VALUE OF INTEREST RATE, REQUEST IN DECIMALS OR CONVERT TO DECIMAL
# ASK FOR VALUE OF COMPOUND FREQUENCY, TIMES PER YEAR
# ASK FOR VALUE OF TIME PERIOD, IN YEAR

#CREATE VARIABLE FOR COMPOUNDING FREQUENCY, CAN BE EMPTY, IT'S A FLOAT
#CREATE VARIABLE FOR TIME PERIOD, IN YEARS, CAN BE EMPTY, IT'S A FLOAT
# CREATE A VARIABLE TO STORE THE TEMPORARY COMPOUND TIME PERIOD
# CREATE A VARIABLE TO STORE THE TEMPOARY MONTHLY INTEREST RATE
# CREATE A VARIABLE TO STORE THE TEMPORARY COMPOUND FACTOR 1 + THE TEMPORARY MONTHLY INTERST RATE
# CREATE VARIABLE TO STORE THE TOTAL TEMPORARY COMPOUND FACTOR


# CALCULATE THE ACCRUED AMOUNT
# PRINT ACCRUED AMOUNT, ROUNDED WITH DOLLAR SIGN

#test values, principal = 10000, interest = 0.04, time period 10, frequency = 12
#test values, princal = 15000, interest = 0.05, time period 5, frequency 2
"""
FOR MY OWN BENEFIT, THE ORIGINAL HACKING CODE
print("hack amount for testing")
x = 15000*((1+(0.04/12))**(12*10))
print(x, "final answer hack for test")
y = 2*5
print(y, " hack compound exponent.")
z = (0.05/2)
print(z, " hack monthly interest rate.")
a = (1+z)
print(a, "hack monthly growth rate." )
b = (a ** y)
print(b, " hack total compound factor.")
c = 15000 * b
print(c, "hack total accrued amount.")
print("conclude hack amounts for testing.\nbegin program.")
"""

accrued_amount = float #CREATE VARIABLE FOR ACCRUED AMOUNT, CAN BE EMPTY, FLOAT

principal_amount = float #CREATE VARIABLE FOR PRINCIPAL BALANCE, CAN BE EMPTY, FLOAT
interest_rate = float #CREATE VARIABLE FOR INTEREST RATE, ANNUAL, CAN BE EMPTY, ITS FLOAT
time_in_years = float #CREATE VARIABLE FOR TIME PERIOD, IN YEARS, CAN BE EMPTY, IT'S A FLOAT
number_payments_per_year = float #CREATE VARIABLE FOR COMPOUNDING FREQUENCY, CAN BE EMPTY, IT'S A FLOAT

# ASK FOR VALUE OF PRINCIPAL AMOUNT, DOLLARS

principal_amount = float(input("Please provide the total principal amount, e.g. $10,000.00 as 10000.\t"))

# ASK FOR VALUE OF INTEREST RATE, REQUEST IN DECIMALS OR CONVERT TO DECIMAL

interest_rate = float(input ("Please provide your interest rate in decimals, e.g. 10% interest is 0.10.\t"))

# ASK FOR VALUE OF COMPOUND FREQUENCY, TIMES PER YEAR

time_in_years = float(input ("Please input the length of time, in years.\t"))

# ASK FOR VALUE OF COMPOUND FREQUENCY, TIMES PER YEAR

number_payments_per_year = float(input ("Please input the number of payments or compound periods per year.\t"))

# CREATE A VARIABLE TO STORE THE TEMPORARY COMPOUND TIME PERIOD

temp_compound_period = time_in_years * number_payments_per_year

#development check of temp_compound_period
#print (temp_compound_period, " temp compound exponent")

# CREATE A VARIABLE TO STORE THE TEMPOARY MONTHLY INTEREST RATE

temp_monthly_int_rate = interest_rate / number_payments_per_year
#development check of temp_monthly_int_rate
#print(temp_monthly_int_rate, " temp monthly interest rate.")
# CREATE A VARIABLE TO STORE THE TEMPORARY COMPOUND FACTOR 1 + THE TEMPORARY MONTHLY INTERST RATE

temp_compound_monthly_factor = 1 + temp_monthly_int_rate
#development check of temp_compound_monthly_factor
#print(temp_compound_monthly_factor, " temp compound_monthly_factor.")
# CREATE VARIABLE TO STORE THE TOTAL TEMPORARY COMPOUND FACTOR

temp_total_compound_factor = temp_compound_monthly_factor ** temp_compound_period
#development check of temp_total_compound_factor
#print(temp_total_compound_factor, " temp total compound factor.")

# CALCULATE THE ACCRUED AMOUNT
accrued_amount = principal_amount * temp_total_compound_factor

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
