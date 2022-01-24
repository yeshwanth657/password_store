# just leaning not related to password store project
try:
    file=open("non-existing one.txt")
    dic={'key':'value'}
    print(dic['nn-existing key'])
except FileNotFoundError as e:
    print(f'there was an error - {e}')
    file=open("non-existing one.txt",mode='w')
    file.write('something')
except KeyError as e:
    print(f'this is a key not found error-{e} ')
else:
    pass
finally:
    h=5
    if h>2:
        raise ValueError('eneter value for this particular variable is wrong')

