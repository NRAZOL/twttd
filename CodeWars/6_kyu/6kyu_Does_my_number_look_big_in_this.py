"""https://www.codewars.com/kata/5287e858c6b5a9678200083c"""


def narcissistic(value):
    narcis = 0
    for i in str(value):
        item = int(i) ** len(str(value))
        narcis += int(item)
    if int(narcis) == value:
        return True
    else: return False