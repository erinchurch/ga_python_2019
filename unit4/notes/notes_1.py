"""
    def __init__(self): #special method
        self.name=''
        self.age = int
        self.grade = 0
        print("creating the object")

    def get_information(self, n, a, g):
        self.name = n
        self.age = a
        self.grade = g
"""

class Person:
    course_name = "Python 101"
    def __init__(self,n,a,g): #special method
        self.name = n
        self.age = a
        self.grade = g
        print("creating the object")

        self.students = {
            1:
                {
                    'name': 'John',
                    'gpa': 3.0,
                    'classes_taken': ('CSC126', 'CSC211', 'CSC326')
                },
            2:
                {
                    'name': 'Mike',
                    'gpa': 2.0,
                    'classes_taken': ('CSC126', 'CSC211', 'CSC326')
                },
            3:
                {
                    'name': 'Stacy',
                    'gpa': 4.0,
                    'Major': 'CS',
                    'classes_taken': ('CSC126', 'CSC211', 'CSC326')
                },
            4:
                {
                    'name': 'Bruce',
                    'gpa': 3.2,
                    'Major': 'CSI',
                    'Minor': 'ISI',
                    'classes_taken': ('CSC211', 'CSC326')
                },
            5:
                {
                    'name': 'Jane',
                    'gpa': 3.7,
                    'Major': 'CSI',
                    'Minor': 'ISI',
                    'classes_taken': ('CSC126', 'CSC211', 'CSC326', 'CSC330', 'CSC490')
                }
        }



    def print_info(self):
        print("name =", self.name)
        print("age = ", self.age)
        print("grade = ", self.grade)
        self.set_course()

    def print_grades(self):
        for keys, values in self.students.items(): #calls the earlier dictionary
            print(keys, values)

    def set_course(self):
        print("Setting the course.")

def main():
    sam = Person("Sam", 27, 99)
    sam.print_grades()
#    sam.get_information("Sam", 27, 99)
#    sam.print_info()
#    john = Person("John", 30, 67)
#    john.print_info()
#    print(sam.course_name)
#    print(john.course_name)

if __name__ == "__main__":
    main()

