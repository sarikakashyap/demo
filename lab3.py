'''
# 1. Modify step #2 from Lab #2 to give employees 1.5 times the hourly rate for any hours worked above 40. 
  
hoursVal = int(input("Enter Hours: "))
rateVal = float(input("Enter Rate: "))

if hoursVal > 40:
    
    wage = rateVal * 40                         # the wage variable calculate the first 40 hours wage
    overtime_hours = hoursVal - 40              # Calculate the  overtime hours

    overtime_rate = rateVal * 1.5               # calculate the overtime rate

    # Calculate the total wage,multiple overtime_rate by overtime_hours and then add it to the existing wage
    Totalwage = wage + overtime_rate * overtime_hours  
else:
    Totalwage = rateVal * hoursVal

print(f"Pay: ${Totalwage}")


# 2. Now re-write step #1 to also include a try/except statement so your program will handle non-numeric 
# values gracefully by letting the user know they put invalid input and exiting the program. 
# (Handle both hours and rate!)because we want to catch both hours and rate,and do not want any of the code to run if something
# invalid was entered. We wrap the entire thing in a
# try/except
try:
    hoursVal = int(input("Enter Hours: "))
    rateVal = float(input("Enter Rate: "))

    if hoursVal > 40:
        
        wage = rateVal * 40                       # the wage variable calculate the first 40 hours wage
        overtime_hours = hoursVal - 40            # Calculate the  overtime hours
    
        overtime_rate = rateVal * 1.5             # calculate the overtime rate

        # Calculate the total wage,multiple overtime_rate by overtime_hours and then add it to the existing wage
        Totalwage = wage + overtime_rate * overtime_hours
    else:
        Totalwage = rateVal * hoursVal

    print(f"Pay: ${Totalwage}")
except:
    print("You entered an invalid number!")


# 3.  Write a program to prompt for a score between  0.0 and 1.0. If the score is out of range (less than 0.0 or greater than 1.0), 
# print an error message. If the score is valid, print their grade using the following table:once again, we do not want any of this code to run if
# they enter an invalid number, so we wrap all of our code in a try/except
'''
try:
    score = float(input("Enter your score: "))
    
    if score <= 0.0 or score >= 1.0:   # it will check the enter score is lies in between the range (0.0 to 0.1)
        print(f"Invalid Score Enter!")
    else:                     # this condition will run only when the valid range is entered
        
        if score >= 0.8:
            print("You got an A!")
        elif score >= 0.7:
            print("You got a B!")
        elif score >= 0.6:
            print("You got a C!")
        elif score >= 0.5:
            print("You got a D!")
        else:
            print("You got an F!")
except:                               # Exception will raised when the user do not entered the number
    print("Invalid Score Enter!")