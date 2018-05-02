import string
string.ascii_uppercase
string.ascii_lowercase
string.digits
string.ascii_letters
alphas = string.ascii_letters + '_'
number = string.digits

print('let`s check')
myinput = input('input your ID:')

if len(myinput) > 1:

    if myinput[0] not in alphas:
        print('first should be letters or _')
    else:
        for i in myinput[1:]:

            if i not in alphas + number:
                print('invalid symbols')
                break
        else:
            print('right')
s = 'abc'
id(s)
s += 'def'
id(s)
