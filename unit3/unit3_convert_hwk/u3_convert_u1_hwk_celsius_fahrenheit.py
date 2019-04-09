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

#get degrees celsius
#equation for converting celius to farhenheit
#carry through celsius from user
#boil point
# freezing point
#fahrenheit equals the boil and freeze applied to celsius
#combine fetching celsius from user and equation
#run it all

def user_input():
    degrees_celsius = float(input("Please provide the degrees celsius you would like to convert to fahrenheit:\t")) #get degrees celsius
#    print("test fetch input:\t", degrees_celsius)
    return degrees_celsius

def celsius_to_fahrenheit():
    degrees_celsius = user_input() #carry through celsius from user
#    print("Test if this is printing the second call.")
    boil_conversion = (180/100) #boiling point
    freeze_conversion = 32 # freezing point
    degrees_fahrenheit = (degrees_celsius * boil_conversion) + freeze_conversion #fahrenheit equals the boil and freeze applied to celsius
    print("You provided:\t", degrees_celsius, "degrees celsius")
    print("The resulting in:\t", degrees_fahrenheit, "degrees fahrenheit.")
    return(degrees_fahrenheit)

def  main():
#    degrees_celsius = user_input()
    degrees_fahrenheit = celsius_to_fahrenheit() #combine fetching celsius from user and equation


if __name__ == "__main__":
    main() #run it all
