'''https://www.codewars.com/kata/545cedaa9943f7fe7b000048'''


def is_pangram(s):
    return True if len(set([i for i in s.lower() if i.isalpha()])) == 26 else False