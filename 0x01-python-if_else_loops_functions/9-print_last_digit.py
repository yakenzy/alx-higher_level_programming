ist_digit(number):
    tmp = int(repr(number)[-1])
    print("{}".format(tmp), end="")
    return tmp
