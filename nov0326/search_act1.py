def linear_search(items, target):
    # TODO: inspect each value with its index
    for index, value in enumerate(items):
        # TODO: return index when target is found
        if value == target:
            return index
    # TODO: return -1 if the loop finishes
    return -1

print(linear_search([10, 4, 12, 8], 12))  # 2