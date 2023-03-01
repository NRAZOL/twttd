"""Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are
multiple elements with the same value, remove the one with a lower index. If you get an empty array/list,
return an empty array/list.

Don't change the order of the elements that are left."""


def remove_smallest(numbers):
    if numbers is None or len(numbers) == 0:
        return numbers
    new_num = numbers.copy()
    new_num.remove(min(numbers))
    return new_num