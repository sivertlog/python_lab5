import py_lab05_p2 as conv
import py_lab05_p1 as check

def binary_to_ip(binary, n=0):
    '''convert binary ip address to decimal format using recursion
    :param binary: binary ip address as a string
    :return: ip address in decimal format as a string
    '''
    part=binary.split(".")
    if n > 2: return str(conv.binary_to_decimal(part[n]))
    return str(conv.binary_to_decimal(part[n])) + "." + binary_to_ip(binary, n+1)

def ip_to_binary(ip, n=0):
    '''convert ip address to binary format using recursion
    :param ip: ip address as a string
    :param n: counter for recursion
    :return: binary ip address as a string
    '''
    part=ip.split(".")
    this_part=conv.decimal_to_binary(int(part[n]))
    this_part=(8-len(this_part))*"0" + this_part
    if n > 2: return this_part
    return this_part + "." + ip_to_binary(ip, n+1)

def ip_convert(ip):
    '''convert ip address between decimal and binary
    :param ip: ip address to be converted as string
    :return: converted ip address as string
    '''
    if check.is_valid_ip(ip):
        return ip_to_binary(ip)
    elif check.is_valid_ip(binary_to_ip(ip)):
        return binary_to_ip(ip)
    else:
        return "Invalid IP Address"

'''
print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"), "test")  # "Invalid IP address"
print(binary_to_ip("11000000.10101000.00000001.00000001"))
print(binary_to_ip("11111111.11111111.11111111.00000000"))
'''

print(ip_convert("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_convert("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_convert("256.1.1.1"))  # "Invalid IP address"
print(ip_convert("11000000.10101000.00000001.00000001"))
print(ip_convert("11111111.11111111.11111111.00000000"))


