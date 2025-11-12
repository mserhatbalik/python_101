# We can use sort() method to PERMANENTLY change the positions of the elements in the list in alphabetical order

car_brands = ["renault", "bugatti", "ferrari", "ford", "audi"]
car_brands.sort()
print(car_brands)

# It is also possible to give additional "reverse" parameter to sort() function to change the ordering of the elements in reverse order
car_brands.sort(reverse=True)
print(car_brands)