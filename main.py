print('hello! this is my code.')

def greeting_name(name:str='fadil')->str:
    return f'halo, {name.upper()}! Senang bertemu denganmu.'

if __name__ == '__main__':
    name1 = greeting_name('miftah')
    name2 = greeting_name()

    print(name1)
    print(name2)