multilineString = '''Hello, This is Noman Sakib
trying to '''
print(multilineString)

print(multilineString[7])

for x in multilineString:
    print(x)

#length of a string
print(len(multilineString))

#Checking a specific word if exist in a string
#in
print("Sakib" in multilineString)

myWord = "Sakib"
if myWord in multilineString:
    print(myWord,"is present")
else:
    print(myWord,"is not present")

# not in
if myWord not in multilineString:
    print("Not exist")
else:
    print("Exist")


#String slicing
myString = "Learn With Sakib"
print(myString[2:5])

print(myString[2:])

print(myString[:5])

print(myString[-5:])

print(myString[-10:-6])

#Modifying string

print(myString.upper())
print(myString.lower())
print(myString.strip()) #removes whitespace from beginning and ending
print(myString.replace("Learn","Teach"))
print(myString.split(" "))

#format String

yourString = "You are so {0},and {1}" #can be used index or not
print(yourString.format("good",21))

