# # We can use range() function inside a wrapped list() function to create list with series of numbers
#
# numbers = list(range(1, 6))
# print(numbers)

# # We can use the third parameter of the range() function to create gaps in generated numbers. In the example below we create only even numbers.
# # The third parameter is the number that is added to the iterated number at each cycle.
#
# even_numbers = list(range(2, 21, 2))
# print(even_numbers)

# Creating squared of numbers through 1 to 10
squared_numbers = []
for number in range(1, 11):
    squared_numbers.append(number ** 2)
print(squared_numbers)