# My solution
# wrong
# def left_rotate_list(arr: list) -> list:
#     last_item = len(arr) - 1
#     first_item = arr[0]
#     arr[0] = arr[last_item]
#     arr[last_item] = first_item
#     return arr


# Time complexity is 0(1) and space complexity is 0(1).
# Time taken 2 mins to write (Time(sec) : 0.017 Memory(MB) : 6.93359375)

# Others

# with array slicing

def left_rotate_list_1(arr: list) -> list:
    arr = arr[1:] + arr[:1]
    return arr


# learning from this is if we don't provide the index to the second value after colon (1:) it will take
# it as the last item(-1) in the index and if you dont specify the first it will start from 0


def left_rotate_list_2(arr: list):
    arr = arr.append(arr.pop(0))
    return arr


def left_rotate_list(arr: list) -> list:
    new_arr = []

    # Handle empty list case. This is important key learning
    if not arr:
        return new_arr

    # Append all elements except the first
    for i in range(1, len(arr)):
        new_arr.append(arr[i])

    # Append the first element to the end
    new_arr.append(arr[0])

    return new_arr
# TC = 0(n) SC = 0(n)


def left_rotate_list_4(arr: list) -> list:
    first = arr[0]
    num = len(arr) - 1

    if not arr:
        return arr

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[num] = first
    return arr

# TC = 0(n) SC = 0(1)


print(left_rotate_list([10, 20, 30, 40]))


print(left_rotate_list([10, 20, 30, 40]))


print(left_rotate_list([10, 20, 30, 40]))
print(left_rotate_list_1([10, 20, 30, 40]))
print(left_rotate_list_1([10, 20, 30, 40]))
