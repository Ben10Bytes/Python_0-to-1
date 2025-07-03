'''Write a program to find out whether a student has passed or failed it is requires a total of 40% and atleast
33% in each subject to pass. Assume 3 subjects and take marks as an input from the users.
'''
Subject1_Marks = int(input("Enter the marks Subject1 : "))
Subject2_Marks = int(input("Enter the marks Subject2 : "))
Subject3_Marks = int(input("Enter the marks Subject3 : "))

#Total_Percentage = (100*(Subject1_Marks + Subject2_Marks + Subject3_Marks))/300
Total_Percentage = (Subject1_Marks + Subject2_Marks + Subject2_Marks)/3


if(Total_Percentage>=40 and Subject1_Marks>=33 and Subject2_Marks>=33 and Subject3_Marks>=33):
    print("You are passed "+ str(Total_Percentage) + "%") 
    #print("You are passed : ",Total_Percentage) #if you want to print without percentage 

else:
    print("You are failed in exam! Better luck next time")
        
