print("I'm \"happy\"!")

# \: escape character
print('I\'m learning\nPython.')

print('\\\n\\')

file ='C:\\Users\\zli'
print(file)
file = r'C:\Users\zli\documents'
print(file)

lyrics = '''Hey Jude,
Don't make it bad
Take a sad song
and make it better'''

print(lyrics)

print('Hey Jude,\nDon\'t make it bad\nTake a sad song\nand make it better')

print()
print()
print()


# modify the code below so it will ask
# user for their age, then print result
# according

age = input('How old are you? >>> ')
# print(type(age))
age = int(age)
country = input('Which country are you in? >>> ')

if age >= 21 and country != 'USA':
    print('Yes, you can.')
else:
    print('Sorry, you cannot.')