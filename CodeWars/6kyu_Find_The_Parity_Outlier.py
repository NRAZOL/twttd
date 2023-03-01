'''https://www.codewars.com/kata/5526fc09a1bbd946250002dc'''


def find_outlier(integers):
    return [max, min][sum(x % 2 for x in integers[:3]) > 1](integers, key=lambda x: x % 2)