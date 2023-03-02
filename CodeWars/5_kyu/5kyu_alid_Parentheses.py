'''https://www.codewars.com/kata/52774a314c2333f0a7000688'''


def valid_parentheses(string):
    count = 0
    for i in string:
        if i == '(': count += 1
        if i == ')': count -= 1
        if count < 0: return False
    return count == 0