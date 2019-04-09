"""

RE-WRITE TO USE FUNCTIONS

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

# create a function for converting fahrenheit to celsius
#function accepts input variable of degrees fahrenheit
# establish variable for celius degrees
# set the freezing point scaler
# set the boiling point scaler
# define formula for converting fahrenheit to celcius

# create a main function
# establishes the variable for fahrenheit degrees, can be positive or negative or zero, cannot be null
#to ask the user for degrees fahrenheit, apply conversion function
#print back to the user what they provided and what the converted degrees are
"""
def fahrenheit_conversion(degrees_fahrenheit):
    degrees_celsius = float
    freeze_point_coversion = 32
    boil_point_conversion = (100/180)
    degrees_celsius = (degrees_fahrenheit - freeze_point_coversion)*boil_point_conversion
    pass
"""

degrees_fahrenheit = float # establishes the variable for fahrenheit degrees, can be positive or negative or zero, cannot be null

degrees_celsius = float # establish variable for celius degrees

def main (): # create a main function
#    degrees_fahrenheit = float # establishes the variable for fahrenheit degrees, can be positive or negative or zero, cannot be null
    degrees_fahrenheit = float(input("Please provide the degrees fahrenheit you wish to convert to degrees celsius.\t"))
#    degrees_celsius = float # establish variable for celius degrees
    freeze_point_conversion = 32 # set the freezing point scaler
    boil_point_conversion = (100 / 180) # set the boiling point scaler
    degrees_celsius = (degrees_fahrenheit - freeze_point_conversion) * boil_point_conversion  # define formula for converting fahrenheit to celcius
    print("You provided: ", degrees_fahrenheit, " degrees farhenheit")
    print("Which is equivalent to: ", degrees_celsius, "degrees celcius.")


if __name__ == "__main__":
    main()