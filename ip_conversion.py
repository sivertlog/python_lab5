import py_lab05_p2 as conv
import py_lab05_p1 as check

def ip_to_binary(ip):
    '''convert ip address to binary format
    ip: ip address as a string
    returns: ip address in binary format as a string
    '''
    bin_ip = ""
    parts=ip.split(".")
    for part in parts:
        bin_ip += ("." +
                   (8-len(conv.decimal_to_binary(int(part))))*"0" +
                   conv.decimal_to_binary(int(part) ))
    return bin_ip.removeprefix(bin_ip[0])


def binary_to_ip(binary):
    '''converts binary ip address to decimal format
    binary: binary ip address as a string
    return: ip address in decimal format as a string
    '''
    dec_ip = ""
    parts=binary.split(".")
    for part in parts:
        dec_ip += "." + str(conv.binary_to_decimal(part))
    return dec_ip.removeprefix(dec_ip[0])

def Rip_to_binary(ip, n=0):
    '''figure out recursion version of ip_to_binary
    ip: ip address as a string
    n: counter for recursion
    return: binary
    '''
    part=ip.split(".")
    this_part=conv.decimal_to_binary(int(part[n]))
    this_part=(8-len(this_part))*"0" + this_part
    if n > 2: return this_part
    return this_part + "." + Rip_to_binary(ip, n+1)



print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"
print(binary_to_ip("11000000.10101000.00000001.00000001"))
print(binary_to_ip("11111111.11111111.11111111.00000000"))

print(Rip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(Rip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(Rip_to_binary("256.1.1.1"))  # "Invalid IP address"
print(binary_to_ip("11000000.10101000.00000001.00000001"))
print(binary_to_ip("11111111.11111111.11111111.00000000"))


