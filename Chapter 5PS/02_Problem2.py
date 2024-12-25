# Write a program to input eight numbers from the user and display all the unique numbers(once).

# 1st Method

empty_set = set()
n1 = int(input("Enter number 1 : "))
empty_set.add(n1)

n2 = int(input("Enter number 2 : "))
empty_set.add(n2)

n3 = int(input("Enter number 3 : "))
empty_set.add(n3)

n4 = int(input("Enter number 4 : "))
empty_set.add(n4)

n5 = int(input("Enter number 5 : "))
empty_set.add(n5)

n6 = int(input("Enter number 6 : "))
empty_set.add(n6)

n7 = int(input("Enter number 7 : "))
empty_set.add(n7)

n8 = int(input("Enter number 8 : "))
empty_set.add(n8)

print(empty_set)


# 2nd Method , the second method is better than 1st method

'''
empty_set = set()

numbers = [
    int(input("Enter number 1 : ")),
    int(input("Enter number 2 : ")),
    int(input("Enter number 3 : ")),
    int(input("Enter number 4 : ")),
    int(input("Enter number 5 : ")),
    int(input("Enter number 6 : ")),
    int(input("Enter number 7 : ")),
    int(input("Enter number 8 : "))
]

empty_set.update(numbers)

print(empty_set)

'''
