''' A spam comment is defined as a text containing following keywords:
"Make a lot of money", "buy now","subscribe this","click this". Write a program to detect this spam'''

P1="Make a lot of money"
P2="buy now"
P3="subscribe this"
P4="click this"

message = input("Write your comment : ")

if ((P1 in message) or (P2 in message) or (P3 in message)):
    print("This is spam!!")

else:
    print("Not spam")  