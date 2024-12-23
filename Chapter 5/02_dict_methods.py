marks={
    "Bent10Bytes":100,
    "Jitu":95,
    "Jites":84,
    0:"Ben10Bytes"
}

#print(marks.items()) # Print all item in your dictonary 
#print(marks.keys()) # Print all key of left side
#print(marks.values()) # Print all values of right side
marks.update({"Ben10Bytes":99,"Sachin":98})
print(marks)

print(marks.get("Ben2")) # .get() is a dictionary method that safely returns None if the key is not found.
print(marks["Ben2"]) # Using marks["Ben2"] directly accesses the key.If the key doesn't exist, Python raises a KeyError.