# Write a program to find out whether a given post is talking about "Ben10Bytes" or not.

post = input("Enter your post: ")

if ("Ben10Bytes".lower() in post.lower()):
    print("This post is talking about Ben10Bytes")

else:
    print("This post is not talking about Ben10Bytes")    
