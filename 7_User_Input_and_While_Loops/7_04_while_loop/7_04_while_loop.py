# While loops are similar to for loops, but they also let us define the counters dynamically
# and play around what to do with the counter inside the loop.

# We define our counter first.
counter = 0

# While loop works similar to an if statement.
# If a certain condition is met, then execute the code inside the while block.
while counter <= 5:
    print(counter)
    counter += 1 # At the last line of a while loop, increase the counter by 1. += is shorthand for "counter = counter + 1"