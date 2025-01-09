''' A spam comment is defined as a text containing following keywords:
"Make a lot of money", "buy now","subscribe this","click this". Write a program to detect this spam'''

P1="Make a lot of money"
P2="buy now"
P3="subscribe this"
P4="click this"

message = input("Write your comment : ")

if ((P1 in message) or (P2 in message) or (P3 in message) or (P4 in message)): #if a certain element is present in a Python object
    print("This is spam!!")

else:
    print("Not spam")  