'''https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec'''


def persistence(n):
    count = 0
    while len(str(n)) > 1:
        count += 1
        n = eval('*'.join(map(str, [i for i in str(n)])))
    return count