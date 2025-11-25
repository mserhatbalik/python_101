# In some cases we would like to know the remainder of divide operation.
# To achieve that we use the modulo (%) operator.
# Modulo operator returns 0 if the 1st number is divisible by the 2nd number perfectly with 0 remainder.
# Module operators returns a number other than 0 if the 1st number is not divisible by the 2nd number perfectly.

print("Welcome to the even and odd number detector program.")
number=int(input("Enter your number\n"))

result = number % 2

# If the result is 0, it means the number is even because it can be divided by 2 perfectly.
# If the result is not 0, it means the number is odd, because it cannot be divided by 2 perfectly.
if result == 0:
    print("Your number is even")
else:
    print("Your number is odd")