def decimal_to_binary(n):
    """converts decimal to binary
    :param n: integer to be converted
    :return: string
    """
    if n == 0: return '0'
    if n == 1: return '1'
    next, digit = divmod(n, 2)
    return (decimal_to_binary(next)) + str(digit)

def binary_to_decimal(b:str):
    """converts binary to decimal
    :param b: string to be converted
    :return: integer
    """
    if b == '': return 0
    place = len(b) - 1
    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))