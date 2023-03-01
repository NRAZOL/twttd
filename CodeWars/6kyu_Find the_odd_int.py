'''https://www.codewars.com/kata/54da5a58ea159efa38000836'''


def find_it(seq):
    return int([str(i) for i in seq if seq.count(i) % 2 != 0][0])