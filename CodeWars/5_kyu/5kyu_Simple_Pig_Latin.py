'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'''


def pig_it(text):
    return ' '.join(''.join([f'{i[1:]}{i[0]}ay']) if i.isalpha() else i for i in text.split())