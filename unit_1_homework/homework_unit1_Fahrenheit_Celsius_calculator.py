"""

3. Write a program that will convert degrees Fahrenheit to degrees Celsius.

The Fahrenheit scale is a temperature scale based on one proposed in 1724 by Dutch–German–Polish physicist Daniel Gabriel Fahrenheit (1686–1736).
The lower defining point, 0 °F, was established as the freezing temperature of a solution of brine made from equal parts of ice, water and salt (ammonium chloride).


The measure for celsius is based on the freezing point of water (0 degrees Celsius, 32 degrees Fahrenheit);
and the boiling point of water, (100 degrees Celsius, 212 degrees Fahrenheit).

To make the measures in degrees equivalent at the freezing point of water, one has to subtract 32 degrees.
to make the measures in degrees equivalent at boiling,
   one has to take the difference in degrees between freezing and boiling (100 degrees in celsius and 180 degrees in fahrenheit)
   100/180, which reduces to the fraction 5/9, which equals approximately 0.5555555555555556

Therefore, to convert celsius to fahrenheit,
   subtract 32 degrees.
   then one has to multiple to the celsius degrees by (180/100), or (9/5), or approximately 0.5555555555555556

Known equivalent values
0C = 32F  The freezing point of water
100C = 212F  The freezing point of water

draft equation

(32F - 32) * (100/180) = 0C
Draft equation
(fahrenheit_degrees - 32) * (100/180) =   celsius_degrees

"""

#create a variable for celsius in degrees, float, cannot be null, but can be negative, positive or zero.

degrees_celsius = float

#create a variable for fahrenheit in degrees, float, cannot be null but can be negative. positive or zero.

degrees_fahrenheit = float


#create a variable for the multiplying factor the conversion at boiling, 180/100, or 9/5, or 1.8, this is a constant.

boiling_pt_factor = 100/180

#create a variable to equate the freezing point, +32 degrees, this is a constant.

freezing_pt_factor = 32

# collect the degrees in celsius

degrees_fahrenheit = float(input("Please provide the temperature you wish to convert, in degrees Fahrenheit.\t"))

# apply the equation to convert to fahrenheit

degrees_celsius = (degrees_fahrenheit - freezing_pt_factor) * boiling_pt_factor

# display back to the user the original input in celsius and the equivalent value in fahrenheit.

print(round(degrees_fahrenheit, 1),"degrees Fahrenheit is equivalent to ", round(degrees_celsius, 1), "degrees Celsius.")