'''
@Author : Priyanka
@Date : 2022-05-02  23:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-05-02  24:00:00
@Title : Calculating employee wage based on their shift using switch case statement.
'''

import random

print("Welcome to the employee wage computation program.")

fullDayEmpHours = 8
halfDayEmpHours = 4
EMP_RATE_PER_HOUR = 20


def empFullDayWage():
    """
        Description:
            Calculating employee full day wage
        Parameter:
            Employee rate per hour and employee full day hours are required to calculate employee full day wage.
        Return:
            Total employee wage and presenty message.
    """
    empWage = fullDayEmpHours * EMP_RATE_PER_HOUR
    return "Employee is full day present and employee wage is ",empWage


def empHalfDayWage():
    """
        Description:
            Calculating employee half day wage
        Parameter:
            Employee rate per hour and employee hours are required to calculate employee wage.
        Return:
            Total employee wage and presenty message.
    """
    empWage = halfDayEmpHours * EMP_RATE_PER_HOUR
    return "Employee is half day present and employee wage is ",empWage


def empPresentyCheck(presentyCheck):
    """
        Description:
             check employee is present or absent.
        Parameter:
             Two random number for employee attendance
        Return:
            returning the check variable
    """
    switcher = {
        0: 'Employee is Absent',
        1: empwageCalculate(random.randint(0, 1))
    }
    return switcher[presentyCheck]


def empwageCalculate(randomCheck):
    """
        Description:
            checking employee half day or full day
        Parameter:
            sending parameter of two random number for checking full day or half day
        Return:
            return function values from full or half day
    """
    switcher = {
        0: empHalfDayWage(),
        1: empFullDayWage()
    }
    return switcher[randomCheck]

empCheck = random.randint(0, 1)
employeeWage = empPresentyCheck(empCheck)

if empCheck == 0:
    print(employeeWage)
else:
    print(employeeWage[0],end="")
    print(employeeWage[1],end="")