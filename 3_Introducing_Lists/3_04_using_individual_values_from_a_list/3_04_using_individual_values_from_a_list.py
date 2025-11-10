# We can access items in a list and use it in f-string formats

countries = ["usa", "russia", "france", "turkey", "japan"]

message = f"My favorite country to visit is {countries[3].title()}."
print(message)