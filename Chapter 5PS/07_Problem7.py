# If the name of 2 friends are same; what will happen to the program in problem 6.

s = {}
Name = input("Enter 1st Name : ")
Lang = input("Favorite Language : ")
s.update({Name:Lang})

Name = input("Enter 2nd Name : ")
Lang = input("Favorite Language : ")
s.update({Name:Lang})

Name = input("Enter 3rd Name : ")
Lang = input("Favorite Language : ")
s.update({Name:Lang})

Name = input("Enter 4th Name : ")
Lang = input("Favorite Language :")
s.update({Name:Lang})

print(s)

# Existing dictionary is update after excution(before same name not include because update is used)