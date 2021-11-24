
#1
def compute_pay(hours,rate):    
        
    if hours > 40:
            
        wage = rate * 40                       # the wage variable calculate the first 40 hours wage
        overtime_hours = hours - 40            # Calculate the  overtime hours
        
        overtime_rate = rate * 1.5             # calculate the overtime rate

            # Calculate the total wage,multiple overtime_rate by overtime_hours and then add it to the existing wage
        Totalwage = wage + overtime_rate * overtime_hours
    else:
        Totalwage = rate * hours

    return Totalwage
    

    

if __name__ =="__main__":
    try:
        hoursVal = int(input("Enter Hours: "))
        rateVal = float(input("Enter Rate: "))
        pay=compute_pay(hoursVal,rateVal)
        print(f"Pay: ${pay}")
    except:
        print("You entered an invalid number!")

'''
#2   
def compute_grade(score):
     
    
    if score <= 0.0 or score >= 1.0:   # it will check the enter score is lies in between the range (0.0 to 0.1)
            ans="Invalid Score Enter!"
    else:                     # this condition will run only when the valid range is entered
            
            if score >= 0.8:
                ans="You got an A!"
            elif score >= 0.7:
                ans="You got a B!"
            elif score >= 0.6:
                ans="You got a C!"
            elif score >= 0.5:
                ans="You got a D!"
            else:
                ans="You got an F!"
    
    return ans    



if __name__ =="__main__":
    try:
        score = float(input("Enter your score: "))
        result=compute_grade(score)
        print(result)
    except:                               # Exception will raised when the user do not entered the number
        print("Invalid Score Enter!")
'''