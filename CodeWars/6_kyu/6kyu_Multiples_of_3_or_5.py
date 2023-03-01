'''https://www.codewars.com/kata/514b92a657cdc65150000006'''


def solution(number):
    num = sum([i if (i % 3 == 0 and i % 5 == 0) else i for i in range(number) if (i % 3 == 0 or i % 5 == 0)])
    return num