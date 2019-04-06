"""
1. Write a program that will compute the area of a rectangle.
Prompt the user to enter the width and height of the rectangle.
Print a nice message with the answer.

The area is measurement of the surface of a shape.
To find the area of a rectangle or a square you need to multiply the length and the width of a rectangle or a square.
A=x * y

to do:
convert the lengths provided into common units of measures (inches, miles, feet, centimeters, kilometers
all the user to provide different units of measure in the input
allow the user to specify the units of measure they have
allow the user to request a specific unit of measure they would like the results to be in.

"""

#create a variable for length of a side of a rectangle, float, cannot be null, cannot be negative

length_rectangle = float

#create a variable for the height of a side of a rectangle, float, cannot be null, cannot be negative

height_rectangle = float

#create a variable for the area, product of the height and length, float, cannot be null, cannot be negative

area_rectangle = float

# ask the user for the length of a side for their rectangle, in centimeters

length_rectangle = float(input("To calculate the area of your rectangle, please provide the length of a side of your rectangle, in centimeters.\t"))

# ask the user for the height of a height for their rectangle, in centimeters

height_rectangle = float(input("To calculate the area of your rectangle, please provide the height of a side of your rectangle, in centimeters.\t"))


#apply the equation for calculating area

area_rectangle = length_rectangle * height_rectangle

# give the user back the value for the area of their rectangle.

print ("For a rectangle with a height of", height_rectangle, "cm and a length of ", length_rectangle, "cm, the area is:", area_rectangle, "cm.")
 