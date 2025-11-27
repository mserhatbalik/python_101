# In some cases, we might not know the parameters a function call might get
# In such cases, we use "**" double asterix to tell python interpreter to create a DICTIONARY of KEY/VALUE pairs with the additional incoming data

# In the example below, we ALWAYS expect f_name and l_name
# During the function definition we also create a dictionary called "additional_info"
# Values other than f_name and l_name will be placed inside this dictionary in a key/value pair fashion
def create_student(f_name, l_name, **additional_info):
    # During the function call the variables will look like this -> ("serhat", "balık", {age: 24, field:"science"}
    # To encapsulate all the information into 1 dictionary; we also add the f_name and l_name into the "additional_info" dictionary
    additional_info["first_name"] = f_name
    additional_info["last_name"] = l_name

    # We return the final version of the "additional_info" dictionary with the f_name and l_name variables also included.
    return  additional_info

student = create_student("serhat", "balık", age=24, field="science")
print(student)