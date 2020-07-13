def do_twice(f, a):
    f(a)
    f(a)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

if __name__ == "__main__":
    do_twice(print_twice, 'spam')
