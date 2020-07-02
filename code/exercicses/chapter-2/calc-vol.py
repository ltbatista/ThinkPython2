def sphere_vol(r):
    pi = 3.14
    vol = (4/3)*pi*r**3
    return vol

def main():
    print("Digite o raio: ")
    raio = int(input())
    volume = sphere_vol(raio)
    print("O volume de uma esfera com raio {} é: {}".format(raio, round(volume,2)))

if __name__ == "__main__":
    main()

