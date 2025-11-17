# In some cases we would like to check for multiple conditions to run an operation.
# Most common checks are AND/OR operators

# AND operator is used to check if ALL conditions apply. If one comparison fails, then the whole IF statement returns FALSE.

gender = "Male"
age = 17  # This 17 value renders the whole if statement FALSE
if (gender.lower() == "male") and (age >= 18):
    print("The person is male and over the age of 18. He is ready for Army!")
else:
    print("The person is not eligible for the Army.")

# OR operator is used to check if ANY of all the the conditions apply. If at least one condition returns TRUE, then the whole if statement returns TRUE.
day = "sunday"
if (day == "saturday" or day == "sunday"):  # If any of the conditions match, if statement will return TRUE.
    print("It is weekend. Chillax.")
else:
    print("Work work work!")
