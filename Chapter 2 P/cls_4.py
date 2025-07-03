"""a=5
b=6
print(a is b)
print(id(a)) This will print the memory address of the integer object 5.
Since 5 is a small integer, it is interned, and the id(a) will be the same as the id(b)."""

#print(id(b))

# list
l=[1,2,4,"abc",True,False]
print(l)
print(type(l))

l2=list([12,23,4,5])
print(l2)
print(type(l2))

print(l[1])
print(l[-1:-3:-1])


