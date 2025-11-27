# This example is the exact copy of the previous section, but with one KEY DIFFERENCE.
# In some cases we would like to preserve the original list.
# In these cases we can pass the COPY of the original list by using [:] slice copy operation.

def print_items(unprinted, completed):
    unprinted.reverse()
    while unprinted:
        current_item = unprinted.pop()
        print(f"Currently printing {current_item}")
        completed.append(current_item)


requested_copies = ["phone case", "robot toy", "key chain"]
printed_copies = []

# We pass the COPY of "requested_copies" list, so the function gets the copy of this list,
# and the operations run inside the function does not affect the original list.
print_items(requested_copies[:], printed_copies)

# "requested_copies" list is still intact, after the function executes.
print(requested_copies)
print(printed_copies)

