# We can put our function definitions into separate files to create cleaner and more structured code
# We use "import" keyword to access the module's function
# In the case below, "pizza" is in the same directory as our main file, so the keyword "import pizza" is enough.
import pizza

# To use the imported function, we need to use the imported module name in front of it.
# In this case, "pizza" module
pizza.make_pizza("medium", "pepperoni", "jambon", "cheese")
pizza.make_pizza("small", "cheese", "mushrooms")