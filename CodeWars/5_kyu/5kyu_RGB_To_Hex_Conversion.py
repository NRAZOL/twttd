"""The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must
be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here."""


def rgb(r, g, b):
    text = ''.join(str(r) + '.' + str(g) + '.' + str(b)).split('.')
    str_rgb = ''
    for i in text:
        if 255 < int(i):
            str_rgb += f'{255: X}'
        elif int(i) <= 0:
            str_rgb += '00'
        elif int(i) < 16:
            str_rgb += f'0{int(i): X}'
        else:
            str_rgb += f'{int(i): X}'
    return str_rgb.replace(' ', '')
