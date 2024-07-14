print('hello! this is my code.')

def greeting_name(name:str='fadil')->str:
    return f'halo, {name.upper()}! Senang bertemu denganmu.'

if __name__ == '__main__':
    names = ['miftah', 'sopian']
    greet = []
    for name in names:
        greet.append(greeting_name(name))
    print(greet)
    