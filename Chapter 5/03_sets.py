e=set() # don't use set={} , because it will create an empty dictionary
s={1,2,3,4,2,2,5}
print(s)

#print(s.count(2)) # That is wrong method to use count function in set , if you want to know how to use count in set please check below
# you can use first of all convert into list and use count function

# Original set with duplicates (set removes duplicates automatically)
s = {1, 2, 3, 4, 2, 2, 5}  # This will become {1, 2, 3, 4, 5}

# Convert set to a list (to allow duplicates)
s_list = [1, 2, 3, 4, 2, 2, 5] 

count_of_2 = s_list.count(2)
print(count_of_2)  # Output: 3 (since 2 appears 3 times)











"""
empty_set = set()
print(empty_set)  # set()
empty_set.add(1)
empty_set.add(2)
print(empty_set)  # {1, 2}

"""