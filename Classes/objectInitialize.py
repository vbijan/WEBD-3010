
# import classExample
# from moduleName(name of the file) import className
from classExample import Student
import shutil

studentOne = Student('John', 'Full Stack', 2025, [55, 67, 89, 44, 99])
studentOne.info()
studentOne.average_grade()
print()
# studentOne.name = 'Wick'
# print(f'{studentOne.name} is enrolled in course {studentOne.course} in year the {studentOne.year}')

studentTwo = Student('Marketing', 'Marketing', 2023, [65, 77, 88, 92, 59])
studentTwo.info()
studentTwo.average_grade()
print()
# studentTwo.name = 'Harry'
# studentTwo.course = 'Marketing'
# studentTwo.year = 2023
# print(f'{studentTwo.name} is enrolled in course {studentTwo.course} in year the {studentTwo.year}')

studentThree = Student('Tom', 'Film Making', 2022, [66, 34, 76, 45, 88])
studentThree.info()
studentThree.average_grade()

# print(f'{studentThree.name} is enrolled in course {studentThree.course} in year the {studentThree.year}')

try:
    shutil.copyfile('classExample.py', 'backup/classExampleBackup.py')
except Exception as e:
    print(e)