# Usually our modules will contain multiple functions.
# In such cases, we might not need to import everything from the module for various reasons.

# In the example below, we use the "from" keyword alongside the import keyword to extract and use a specific function inside a module
from pizza import make_pizza

# When we directly import the function. We don't need to use the "." notation and chain it with the module name as we did in the previous section.
make_pizza("medium", "pepperoni", "jambon", "cheese")
make_pizza("small", "cheese", "mushrooms")
