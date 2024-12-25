#if language of two friends are same; what will happen to the program 
# Answer-- The language of two friends are same that means values can same but keys are not same because if keys are same so it will update 
# the last keys for the reason behind .update function is used
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

