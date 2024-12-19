# Write a program to fill in a letter templete given below with name and date.

letter='''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Ben10bytes").replace("<|Date|>","17 Sep 2024"))