def left_rotate_list(arr: list) -> list:
    last_item = len(arr) - 1
    first_item = arr[0]
    arr[0] = arr[last_item]
    arr[last_item] = first_item
    return arr


print(left_rotate_list([10, 20, 30, 40]))