def calc_price(cb_price, copies):
    ## calculates the 40% off
    price = cb_price*0.6
    ## calculates the shipping cost
    if copies > 1:
        addcopy = (copies-1)*0.75
        price_add = price*(copies-1)
    else:
        addcopy = 0
        price_add = 0
    return price + addcopy + price_add + 3

def main():
    cb_price = 24.95
    qtd_cp = 60
    price = calc_price(cb_price, qtd_cp)
    print(round(price,2))

if __name__ == "__main__":
    main()

