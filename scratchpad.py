for x in range(1,11):
    print(x)

dictionary = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

print(dictionary['I'])

test = {'test': 'faeiled'}
if test == 'failed':
    print('yes')
else:
    print('no')

test = 'failed'
if test == 'failed':
    print('yes')
else:
    print('no')

print(1,2)

dictionary = {'1': {'2':1}}
print(dictionary['1'])

if 1 in dictionary:
    if 2 in dictionary['1']:
        print('yes')
    else:
        print('no')
else:
    print('no')
