import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class Challange:
    # print the version of pandas. (Error here)
    print(pandas.__version__)

    def __init__(self, student_name=None, student_class=None):
        student_name =  self.student_name
        student_class = self.student_class

    def calculator(self, numOne = float, numTwo = float, operation = str) -> float:
        if operation =='+':
            result = numOne + numTwo
        elif operation == '-':
            result = numOne - numTwo
        elif operation == '*': 
            result = numOne '*' numTwo
        elif operation == '/':
            '''
                Task: Should not receive an error when I try to divide with zero.
            '''
            result = numOne / numTwo
        else:
            # only +, -, *, / should be accepeted. 
            raise ValueError("Invalid operation. Choose from '+', '-', '*', '/'.")
        return result
    
    def info(self):
        print('Welcome {self.student_name} to the {self.course} challenge!')

    #static method in python
    def greet():
        print('Greeting form the challage One ')

    '''
        Task: Implement Specific error except in the below function, it accepts only 2D array.
    '''
    # accepts a list(2D array) parameter. Implement
    def linear_regression(self, X):
        X = np.array(X)
        y = np.dot(x, np.array([1, 2])) + 3
        reg = LinearRegression().fit(X, y)

        # Predictions
        predictions = reg.predict(np.array([[3, 5]]))

        print(f"Coefficient: {reg.coef_}")
        print(f"Intercept: {reg.intercept_}")
        print(f"Prediction for [[3, 5]]: {prediction}")

    # print Fibonacci series
    '''
        Task: Fibonacci series must be printed using sequential assignment like below.
    '''
    def fibo(self, n):
        a = 0
        b = 1
        while a < n:
            print(a, end=' ')
            a = b
            b = a+b
        print()