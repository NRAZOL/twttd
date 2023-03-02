'''https://www.codewars.com/kata/52597aa56021e91c93000cb0'''


def move_zeros(lst):
    return [i for i in lst if i != 0 ] + [0] * lst.count(0)