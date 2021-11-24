'''Your task in this assignment is to convert an input number into an output string. 
The output strings will be primary colours that correspond to certain potential 
factors. A factor is a number that evenly divides into another number, leaving no 
remainder. (Hint: modulo operator %)
'''

# The rules for colours are that if you input a number that has:
# a) 5 as a factor, the word "Red" should print
# b) 7 as a factor, the word "Blue" should print
# c) 9 as a factor, the word "Yellow" should print
# d) Does not have any 5, 7, or 9, the word "Black" should print

# try:

#     number1=input("Enter a number: ") 
#     number=int(number1)  #converting the enter value into number
#     count=0              #taking the count variable, if number is not the factor of 5,7,9 then count remain 0 so it print Black
    
#     for num in range(5,10,2): # for loop having numnber 5,7,9
#         factor=number%num     # calculate the factor ,
#         if (factor==0 ):      #  when the remainder of the number is zero then that num is the factor of the number
#             #now check the number and print that Color and increase count variable
#             if(num==5):       
#                 print("Red",end="")
#                 count =+1     #increment the count variable by 1
#             elif(num==7)  :
#                 print("Blue",end="")  
#                 count =+1 
#             elif(num==9):
#                 print("Yellow",end="")
#                 count =+1
        
#     if count==0:         # this coundition is execute when the value of the count remain zero
#         print("Black")   # i.e number has no factor in range of 5,7,9
# except:
#     print(number1)


         
            
try:
    number1=input("Enter a number: ") 
    number=int(number1)
    if(number%5==0):
        print("Red",end="")
        
    if(number%7==0):
        print("Blue",end="")
    if(number%9==0):
        print("Yellow",end="")
    if(number%5!=0 and number%7!=0 and number%9!=0 ):
        print("Black")

except:
    print(number1)

   
        

            
          