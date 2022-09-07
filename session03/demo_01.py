# print("Hello, world!")

# print('Hey Jude', "don't make it bad")

# print('The total number of overall medals in Tokyo 2020 is', 39 + 41 + 33)

# name = input()
# print(name)

message = "I did something cool today!"
n = 100
pi = 3.14

# = assignment

# print(n + 200)

lyrics = 'Naah, na na nanana naah, nanana naah, hey Jude.\n' * 10

# print(lyrics)


# s = [1, 2]
# print(s)

name = 'world'
# print('Hello,', name, '!')
# print('Hello,', name +'!')

# f-string
# print(f'Hello, {name}!')

pi = 3.1415926

print(f'Pi equals {pi:.5f}.')
print(f'Pi equals {pi:8.5f}.')
print(f'Pi equals {pi:8.2f}.')

print()
items = {"orange": 3.99, "ice_cream": 5.99, "iphone": 999.99}

for name, price in items.items():
    print(f'{name:12}: ${price:7.2f}')
print()

# a = 2021

# # binary
# print(f'{a:b}')

# # hexadecimal
# print(f"{a:x}")

# # octal
# print(f"{a:o}")

# # scientific
# print(f"{a:e}")


s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'|{s1:>10}|')
print(f'|{s2:>10}|')
print(f'|{s3:>10}|')
print(f'|{s4:>10}|')
print(f'|{s1:<10}|')
print(f'|{s2:<10}|')
print(f'|{s3:<10}|')
print(f'|{s4:<10}|')
print(f'|{s1:^10}|')
print(f'|{s2:^10}|')
print(f'|{s3:^10}|')
print(f'|{s4:^10}|')
