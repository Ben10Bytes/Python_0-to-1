'''
Create an empty dictionary. Allow 4 friends to enter their favorite languages as value and use key as their names. Assume that the name are 
uniques
'''

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