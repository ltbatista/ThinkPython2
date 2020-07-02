def calc_price(cb_price, copies):
    ## calculates the 40% off
    price = cb_price*0.6
    ## calculates the shipping cost
    price = price + 3
    if copies > 1:
        addcopy = (copies-1)*0.75
    else:
        addcopy = 0
    return price + addcopy

def main():
    cb_price = 24.95
    qtd_cp = 60
    price = calc_price(cb_price, qtd_cp)
    print(price)

if __name__ == "__main__":
    main()

