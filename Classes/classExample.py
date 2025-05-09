# class is a blueprint to crete an object
# object is an instance of a class

class Student:
    # name

    # construtor method, magic/dunder method __init__
    def __init__(self, name=None, course=None, year=None, grades=None):
        print('Object is initialized')  
        self.name = name
        self.course = course
        self.year = year
        self.grades = grades

    # method to print the information of the students
    def info(self):
        print(f'{self.name} is a student from {self.course} enrolled in the year {self.year}.')

    # average is sum of datas divide by total number of data provided
    def average_grade(self):
        #check if the grades are provided to handle the error
        if self.grades:
            avg = sum(self.grades)/len(self.grades)
            print(f'The average grade of {self.grades} is {avg}')
        else:
            print('Grades not provided')

# objects can be created on the same file if we are outside the class
# studentOne = Student()
# print(studentOne.name)


