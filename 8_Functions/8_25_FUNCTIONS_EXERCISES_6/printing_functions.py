def print_items(unprinted, completed):
    unprinted.reverse()
    while unprinted:
        current_item = unprinted.pop()
        print(f"Currently printing {current_item}")
        completed.append(current_item)