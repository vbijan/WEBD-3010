# print('Hello World!')

# variables
# num1 = 2
# num2 = 3
# sum = num1+num2
# print(sum)

marks = [1, 3, 5, "John", 7, 8, 99, 56]

# print(marks)
# print(marks[0])
# print(marks[3])

# print(marks[-1])
# print(marks[len(marks)-1])
# f strings
# print(f'The length of my lists is {len(marks)}')

#slicing
print(marks[:])
print(marks[1:])
print(marks[1:3])

#jumpindex
print(marks[1:8:2])

marks.append(False)

print(marks)

if 99 in marks:
    print(f'The number is there on the lists. {marks}')
else:
    print('the number is not present')


