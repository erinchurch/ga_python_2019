"""

2. Write a program that will convert degrees Celsius to degrees Fahrenheit.

The measure for celsius is based on the freezing point of water (0 degrees Celsius, 32 degrees Fahrenheit);
and the boiling point of water, (100 degrees Celsius, 212 degrees Fahrenheit).

To make the measures in degrees equivalent at the freezing point of water, one has to add 32 degrees.
to make the measures in degrees equivalent at boiling,
   one has to take the difference in degrees between freezing and boiling (100 degrees in celsius and 180 degrees in fahrenheit)
   180/100, which reduces to the fraction 9/5, which equals 1.8

Therefore, to convert celsius to fahrenheit,
   one has to multiple to the celsius degrees by (180/100), or (9/5), or 1.8
   then add 32 degrees.

Known equivalent values
0C = 32F  The freezing point of water
100C = 212F  The freezing point of water

draft equation
(0C * 9/5) + 32 = 32F
Draft equation
celsius_degrees * (9/5) + 32 = fahrenheit_degrees

"""

#create a variable for celsius in degrees, float, cannot be null, but can be negative, positive or zero.

degrees_celsius = float

#create a variable for fahrenheit in degrees, float, cannot be null but can be negative. positive or zero.

degrees_fahrenheit = float


#create a variable for the multiplying factor the conversion at boiling, 180/100, or 9/5, or 1.8, this is a constant.

boiling_pt_factor = 180/100

#create a variable to equate the freezing point, +32 degrees, this is a constant.

freezing_pt_factor = 32

# collect the degrees in celsius

degrees_celsius = float(input("Please provide the temperature you wish to convert, in degrees Celsius.\t"))

# apply the equation to convert to fahrenheit

degrees_fahrenheit = (degrees_celsius * boiling_pt_factor) + freezing_pt_factor

# display back to the user the original input in celsius and the equivalent value in fahrenheit.

print(round(degrees_celsius, 1),"degrees celsius is equivalent to ", round(degrees_fahrenheit,1), "degrees fahrenheit.")

