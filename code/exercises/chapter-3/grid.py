def print_mais():
    print('+', end = ' ')

def print4traco():
    print('-'*4, end = ' ')

def print1pipe():
    print('|', end = ' ')

def print1espaco():
    print(' ', end = ' ')

def print4espaco():
    print(' '*4, end = ' ')

def linha_traco():
    print_mais()
    print4traco()

def linha_espaco():
    print1pipe()
    print4espaco()

def do_four(f):
    f()
    f()
    f()
    f()

def linha4brancopipe():
    do_four(linha_espaco)
    print1pipe()
    print('\n')

def draw_grid():
    do_four(linha_traco)
    print_mais()
    print('\n')
    do_four(linha4brancopipe)

if __name__ == '__main__':
    do_four(draw_grid)
    do_four(linha_traco)
    print_mais()
