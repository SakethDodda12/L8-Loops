string = input("please enter a string:")
string2 = ('')

for i in string:
    string2 = i + string2

print("\n The original string: ", string)
print("Reversed string: ", string2)