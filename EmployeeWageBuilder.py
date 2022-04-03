'''
@Author : Priyanka
@Date : 2022-05-02  19:38:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-02  19:44:00
@Title : Calculating daily employee wage.
'''

import random

print("Welcome to the employee wage computation program.")

IS_Full_Time = 1
EMP_RATE_PER_HOUR = 20
empHours = 0
empWage = 0
empCheck = random.randint(0,1)

if empCheck == IS_Full_Time:
    print("Employee is present")
    empHours = 8
else:
    print("Employee is absent")
    empHours = 0
empWage = empHours * EMP_RATE_PER_HOUR
print("Employee wage is",empWage)