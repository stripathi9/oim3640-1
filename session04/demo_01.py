print("I'm ok!")

print("I\'m \"ok\"!")
# \: escape character

print('I\'m learning\nPython')

print('\\\n\\')

# C:\Users\zli\documents
print('C:\\Users\\zli\\documents')

print(r'C:\Users\zli\documents')

print(
    '''line1
line2
line3'''
)
print('line1\nline2\nline3')



# Modify the code below so it will ask
# the user for their age first, then 
# print the result accordingly
age = input("How old are you? >>> ")
country = input('Which country are you in? >>>')
age = int(age)

if age >= 21 or country != "USA":
    print('Yes, you can!')
else:
    print('Sorry, you cannot.')