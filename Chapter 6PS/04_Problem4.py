# Write a program to find whether a given username contains less than 10 characters or not.

user_name = input("Enter Username : ")

if (len(user_name)<10):
    print("Valid Username")
    print(len(user_name))

else:
    print("Not valid Username")    