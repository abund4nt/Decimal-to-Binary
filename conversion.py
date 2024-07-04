def binary_to_decimal(n):
    if n == 0:
        return('0')

    binary = ''
    while n > 0:
        residue = n % 2
        binary = str(residue) + binary
        n = n // 2
    return binary

if __name__ == '__main__':
    n = int(input("Enter a number to convert to binary: "))
    print(f"The number {n} converted into binary is {binary_to_decimal(n)}")

