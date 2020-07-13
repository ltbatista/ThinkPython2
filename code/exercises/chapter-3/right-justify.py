def right_justify(s):
    print(((70 - len(s))*' ')+s)

if __name__ == "__main__":
    print('right-justify\ninput a string: ')
    inps = input()
    right_justify(inps)
