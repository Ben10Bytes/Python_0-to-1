# Methods in Python

a = "Forgive me!"
print(a.upper()) # All word change in capital letter
print(a.lower()) # All word change in small letter
print(a.capitalize()) # Starting of the letter change in capital and rest will be small
print(a.title()) # The first letter of each word will be capitalized 
print(a.find("g")) # Find index position
print(a.find("z")) # If not find index position the compiler return -1

b= "rAJAN"
print(b.capitalize())

c = "   Welcome to the coding world   "
print(c.strip()) # Removing whitespace from the beginning or the end
print(c.replace("W", "Z")) # The replace() method replaces a string with another string

# I also using strip and replace methods together

print(c.strip().replace("Welcome", "Go"))
print(c.replace("Welcome", "Go").strip()) # Both line will be same