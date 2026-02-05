"""
x = 10

def change():
    x = 5   # Python thinks this is a NEW local variable. The output will be 10

change()
print(x)

"""


x = 10

def change():
    global x
    x = 5   # now global x is modified

change()
print(x)
