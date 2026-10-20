''' Trying to develop an app that can convert number types(decimal, binary, octal, and hexa-decimal) into any other type there is'''

def binary_decimal():
    while True:
        binary_num = input("Enter a binary number: ")
        try:
            int(binary_num, 2)
            break
        except ValueError:
            print("Please enter valid binary number and Try again.")


    Bdigits = [int(bit) for bit in binary_num]
    decimals = []

    for digit in Bdigits:
        decimals.append(Bdigits[digit] * 2**len(Bdigits))

    print("The decimal equivalent of binary number binary_num is: ", sum(decimals))  

def decimal_binary():
    while True:
        decimal_num = input("Enter a decimal number: ")
        try:
            decimal_num = int(decimal_num)
            break
        except ValueError:
            print("Please enter valid decimal number and Try again.")
    Ddigits = decimal_num
    binary = []

    if decimal_num == 0:
        print("The binary equivalent of decimal number 0 is: 0")
    while decimal_num > 0:
        binary.append(decimal_num % 2)
        decimal_num = decimal_num // 2
    print("The binary equivalent of decimal number decimal_num is: ", binary[::-1])


def decimal_to_hex():
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"

    while True:
        decimal_num = input("Enter a decimal number: ")

        try:
            decimal_num = int(decimal_num)

            if decimal_num < 0:
                print("Please enter a non-negative decimal number.")
                continue

            break

        except ValueError:
            print("Please enter a valid decimal number and try again.")

    hex_digits = []

    if decimal_num == 0:
        print("The hexadecimal equivalent is: 0")
        return

    while decimal_num > 0:
        num = decimal_num % 16

        if num == 10:
            hex_digits.append(A)
        elif num == 11:
            hex_digits.append(B)
        elif num == 12:
            hex_digits.append(C)
        elif num == 13:
            hex_digits.append(D)
        elif num == 14:
            hex_digits.append(E)
        elif num == 15:
            hex_digits.append(F)
        else:
            hex_digits.append(str(num))

        decimal_num = decimal_num // 16

    print("The hexadecimal equivalent is:", "".join(hex_digits[::-1]))


decimal_to_hex()

##print(Ddigits)
##decimal_binary()
##binary_decimal()