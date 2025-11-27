# The lists we pass as function arguments are the original copies.
# Any operation we execute inside a function which changes the structure and data of these lists will become permanent.

def print_items(unprinted, completed):
    unprinted.reverse()
    while unprinted:
        current_item = unprinted.pop()
        print(f"Currently printing {current_item}")
        completed.append(current_item)


requested_copies = ["phone case", "robot toy", "key chain"]
printed_copies = []

print_items(requested_copies, printed_copies)
print(requested_copies)
print(printed_copies)

