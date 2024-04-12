file = open('<Binary File Pathname Goes Here>').read().strip().split(' ')


def modToStart1(number, mod):
    return '10' * (number // mod) + ('1' * (number % mod))


def modToStart0(number, mod):
    return '01' * (number // mod) + ('0' * (number % mod))


for val in file:
    if val[-1] == "'":
        newVal = val.replace("'", '')
        print(modToStart1(int(newVal), 2), end='')
    elif val[0] == ".":
        newVal = val.replace('.', '')
        newVal = newVal[:-1]
        print(val[-1] * int(newVal))
    else:
        print(modToStart0(int(val), 2), end='')
