'''
@Author : Priyanka
@Date : 2022-05-02  19:25:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-02  19:35:00
@Title : Checking employee is present or not.
'''

import random

print("Welcome to the employee wage computation program.")

IS_Full_Time = 1
empCheck = random.randint(0,1)

if empCheck == IS_Full_Time:
    print("Employee is present")
else:
    print("Employee is absent")