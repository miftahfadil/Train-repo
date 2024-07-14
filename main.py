print('hello! this is my code.')

def greeting_name(name:str='fadil')->None:
    print(f'halo, {name.upper()}! Senang bertemu denganmu.')

if __name__ == '__main__':
    names = ['miftah', 'sopian']
    for name in names:
        greeting_name(name)
    greeting_name()