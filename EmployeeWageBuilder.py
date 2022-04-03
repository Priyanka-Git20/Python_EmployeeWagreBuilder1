'''
@Author : Priyanka
@Date : 2022-05-02  19:46:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-02  19:54:00
@Title : Calculating employee wage based on their shift.
'''

import random

print("Welcome to the employee wage computation program.")

IS_Full_TIME = 1
IS_PART_TIME = 2
EMP_RATE_PER_HOUR = 20
empHours = 0
empWage = 0
empCheck = random.randint(0,2)

if empCheck == IS_Full_TIME:
    print("Employee is full day present")
    empHours = 8
elif empCheck == IS_PART_TIME:
    print("Employee is half day present")
    empHours = 4
else:
    print("Employee is absent")
    empHours = 0
empWage = empHours * EMP_RATE_PER_HOUR
print("Employee wage is",empWage)