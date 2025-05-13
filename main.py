import task

# object initialization and implementaion. (Error here)
a = Challange('Jogn', 'Full Stack Web Development')

# Calling the static method of the class static methods cannot be accessed directly my an object.
a.greet()

a.linear_regression([1,2])

# inputs for the calculator.
numOne = input("Enter number one: ")
numTwo = input("Enter number Two: ")
operation = int(input("Enter the operation that you want: "))
print(f'The result for the operation is {a.calculator(numOne, numTwo, operation)}.')

# print Fibonacci Series
a.fibo(100)

'''
    Task: Print following pattern
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5
'''
rows = "5"  
for i in range(0, rows):  
    for j in range(1, j + 1):  
        print(j end=' ')  
    print("")  
print("Done!")  