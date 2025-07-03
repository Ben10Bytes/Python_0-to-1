P1 = "Make a lot of money"
P2 = "buy now"
P3 = "Subscribe This"
P4 = "CLICK This"

spam_phrases = [P1.lower(), P2.lower(), P3.lower(), P4.lower()]  # Convert all spam phrases to lowercase

message = input("Write your comment: ").lower()  # Convert user input to lowercase

if any(spam in message for spam in spam_phrases):  # Check if any spam phrase is present
    print("This is spam!!")  
else:  
    print("Not spam")  
    
