'''https://www.codewars.com/kata/546f922b54af40e1e90001da'''


import string
def alphabet_position(text):
    s = '{}'.format(string.ascii_letters[:26])
    slovar = {i: s.index(i)+1 for i in '{}'.format(string.ascii_letters[:26])}
    return ' '.join(str(slovar[i]) for i in text.lower() if i.isalpha())