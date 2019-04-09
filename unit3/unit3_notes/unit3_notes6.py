class Student:
    uni = "Oxford" #class variables are shared by everyone, everyone belongs to it
    def get_name(self, s_name, s_age, s_city): #method in class, () are local variables to the class
        self.name = s_name #object variables or fields, are the variables in a method
        self.age = s_age
        self.city = s_city
        print(self.name)
        print(self.age)

john = Student() #create new object in the type of student()
john.get_name("John",25, "New York") #can now use any methods in that class of student and give it arguments, that will become part of the object


#mike = Student()
#mike.get_name("Mike")

susan = Student()
susan.get_name("Susan", 25, "London")
print(susan.name)
print(susan.age)
print(john.uni)
print(susan.uni)

#you can either call the entire method and populate information for an object, opportunity to fill out all the items at once

#or you can populate the object information piece by piece

#self means that every object in the class have that variable or field