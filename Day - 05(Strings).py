#Day - 05(Strings)
#Example 1 – Print Name
name = "sanjeev"
print(name)
#Example 2 – First Character
name = "sanjeev"
print(name[0])
#Example 3 – Last Character
name = "sanjeev"
print(name[-1])
#Example 4 – Length
name = "sanjeev"
print(len(name))
#Example 5 – Uppercase
name = "sanjeev"
print(name.upper())
#Example 6 – Lowercase
name = "sanjeev"
print(name.lower())
#Example 7 – Count Letter 'a'
word = "aaabadyaa"
count = 0
for x in word:
    if x == "a":
        count += 1
print(count)
#Example 8 – Reverse String
name = "sam"
print(name[::-1])
