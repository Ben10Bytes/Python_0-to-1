'''
marks = {"Alice": 90, "Bob": 85}
print(marks.get("Bob"))      # 85
print(marks.get("Eve", 0))   # 0 (default if not found)

marks = {"Alice": 90, "Bob": 85}

if 90 in marks.values():
    print("Value 90 found")
else:
    print("Value 90 not found")
'''

marks = {"Alice": 90, "Bob": 85, "Eve": 88}

# Remove the last item
removed_item = marks.popitem()

print(removed_item)  # ('Eve', 88)
print(marks)         # {'Alice': 90, 'Bob': 85}
Ha