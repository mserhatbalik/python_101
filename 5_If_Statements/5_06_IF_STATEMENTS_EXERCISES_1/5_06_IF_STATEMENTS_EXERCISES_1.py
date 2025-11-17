"""
5-1. Conditional Tests: Write a series of conditional tests.
Print a statement describing each test and your prediction for the results of each test.
Your code should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

Look closely at your results, and make sure you understand why each line evaluates to True or False.
Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

"""

# VARIABLES FOR THE TESTS
language = "Python"
year = 2023
is_learning = True

# Test 1
print("Is language == 'Python' TRUE OR FALSE - I predict TRUE")
print(language == "Python")

# Test 2
print("\nIs language != 'Java' - I predict TRUE, because it is not java, and we also use 'not' operator" )
print(language != 'java')

# Test 3
print("\nIs year > 2000 - I predict True, because year is greater than 2000")
print(year > 2000)

# Test 4
print("\nIs is_learning == True, I predict TRUE because it is True")
print(is_learning == True)

# Test 5
print("\nIs year >= 2023, I predict TRUE because year is equal/greater than 2023")
print(year >= 2023)

# Test 6
print("\nIs language == 'python', I predict FALSE because cases don't match")
print(language == "python")

# Test 7
print("\nIs year 2024, I predict FALSE because year is equal 2023")
print(year == 2024)

# Test 8
print("\nIs year < 2023, I predict FALSE because year is 2023")
print(year < 2023)

# Test 9
print("\nIs is_learning == False, I predict FALSE because is_learning is TRUE")
print(is_learning == False)

# Test 10
print("\nIs language == 'JavaScript, I predict FALSE, because language is Python")
print(language == "JavaScript")