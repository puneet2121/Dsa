# def separate_list(arr:list):

#     odd_list = []
#     even_list = []
#     for number in arr:
#         if number % 2 == 0:
#             even_list.append(number)
#         else:
#             odd_list.append(number)
#     print(even_list,odd_list)

# separate_list([1,2,2,3,5])

# def get_smaller_elements(arr:list, x):
#     new_list = []
#     for number in arr:
#         if number < x:
#             new_list.append(number)
#     return new_list

# print(get_smaller_elements([5,10,13,15,12,21],20))

# def find_smaller(arr:list, x):
#     new_list = [num for num in arr if num < x]
#     print(new_list)

# find_smaller([1,2,3],2)


# def sort_number(arr:list)-> tuple:
#     even_list = [num for num in arr if num % 2 == 0]
#     odd_list = [num for num in arr if num % 2 != 0]
#     return odd_list, even_list
# odd,even = sort_number([2,5,6,9])
# print(even)


# word = 'geeksforgeeks'

# l1 = [x for x in word if x in 'aeiou']
# print(l1)


# def largest_element(arr:list):
#     if not arr:
#         return None
#     number = 0
#     for i in arr:
#         if i > number:
#             number = i
#     return number

# arr = [1,41,7,2,45,12,55]
# print(largest_element(arr))


# def second_largest_element(arr: list):
#     if len(arr) <= 1:
#         return None

#     lar = secondlar = None

#     for i in arr:
#         if lar is None or i > lar:
#             secondlar = lar
#             lar = i
#         elif secondlar is None or i > secondlar and i != lar:
#             secondlar = i

#     return secondlar

# arr = [ 4, 4, 4]
# print(second_largest_element(arr))


# def is_sorted(arr:list):
#     i = 1
#     while i < len(arr):
#         if arr[i] < arr[i - 1]:
#             return False
#         i = i + 1
#     return True

# arr = [ 4, 4, 4]
# print(is_sorted(arr))

# def reverse_a_list(arr:list):
#     # arr = arr[::-1]
#     # return arr
#     # new_array = []
#     # num = len(arr) - 1
#     # for i in range(0, len(arr)):
#     #     new_array.append(arr[num])
#     #     num = num - 1
#     # return new_array

#     s = 0
#     le = len(arr) - 1

#     while s < le:
#         arr[s], arr[le] = arr[le], arr[s]
#         s = s + 1
#         le = le - 1
#     return arr

# arr = [1,2,3,7,6]

# print(reverse_a_list(arr))

# def remove_duplicates(arr: list) -> list:
#     # i = 0
#     # while i < len(arr) - 1:
#     #     if arr[i] == arr[i + 1]:
#     #         arr.pop(i)
#     #     else:
#     #         i += 1
#     # return arr
#     num = len(arr)
#     s = 1
#     for i in range(1, num):
#         if arr[s - 1] != arr[i]:
#             arr[s] = arr[i]
#             s = s + 1
#     return arr

# Test
# arr = [10, 20, 30, 40, 40]
# print(remove_duplicates(arr))  # Output: [10, 20, 30, 40]


