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
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15
    while True:
        decimal_num = input("Enter a decimal number: ")
        try:
            decimal_num = int(decimal_num)
            break
        except ValueError:
            print("Please enter valid decimal number and try again.")

    Ddigits = [int(bit) for bit in decimal_num]
    hex = []
        
    if decimal_num == 0:
        print("The hexdecimal equivalent for a decimal number 0 is: 0" )
    while decimal_num > 0:
        num = decimal_num % 16
        if num == 10:
            hex.append(A)
        elif num == 11:
            hex.append(B)
        elif num == 12:
            hex.append(C)
        elif num == 13:
            hex.append(D)
        elif num == 14:
            hex.append(E)
        elif num == 15:
            hex.append(F)
        else:
            hex.append(num)
        decimal_num = decimal_num // 2

print("The hexadecimal equivalent of decimal number decimal_num is: ", hex[::-1])

decimal_to_hex()
##print(Ddigits)
##decimal_binary()
##binary_decimal()