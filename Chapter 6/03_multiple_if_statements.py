
a = int(input("Enter your age : "))

# 1st if statement
if (a%2==0):
    print("a is even")

else:
    print("a is odd")    
# End of the 1st if statement

# 2nd if statement
if (a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif (a<0):
    print("The age you have entered does not exist")

elif (a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")
# End of  the 2nd if statement

print("End of the program")      