'''Write a program to find out whether a student has passed or failed it is requires a total of 40% and atleast
33% in each subject to pass. Assume 3 subjects and take marks as an input from the users.
'''

subjects1_marks=int(input("Enter marks subject1 : "))
subjects2_marks=int(input("Enter marks subject2 : "))
subjects3_marks=int(input("Enter marks subject3 : "))

total_percentage=(100*(subjects1_marks+subjects2_marks+subjects3_marks))/300

if (total_percentage>=40 and subjects1_marks>=33 and subjects2_marks>=33 and subjects3_marks>=33):
    print("You are passed"+str(total_percentage)+"%")

else:
    print("You are failed!"+str(total_percentage)+"%")    


