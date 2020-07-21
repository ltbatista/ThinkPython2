def check_fermat(a, b, c, n):
    if n >= 2:
        if (a**n+b**n) == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")

def input_number():
    a = int(input('Digit o valor de a: \n'))
    b = int(input('Digit o valor de b: \n'))
    c = int(input('Digit o valor de c: \n'))
    n = int(input('Digit o valor de n: \n'))
    check_fermat(a, b, c, n)

if __name__ == "__main__":
    input_number()

