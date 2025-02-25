import py_lab05_p2 as conv
import py_lab05_p1 as check

def ip_to_binary(ip):
    bin_ip = ""
    parts=ip.split(".")
    for part in parts:
        bin_ip += ("." +
                   (8-len(conv.decimal_to_binary(int(part))))*"0" +
                   conv.decimal_to_binary(int(part) ))
    return bin_ip.removeprefix(bin_ip[0])


def binary_to_ip(binary):
    dec_ip = ""
    parts=binary.split(".")
    for part in parts:
        dec_ip += "." + str(conv.binary_to_decimal(part))
    return dec_ip.removeprefix(dec_ip[0])

print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"
print(binary_to_ip("11000000.10101000.00000001.00000001"))
print(binary_to_ip("11111111.11111111.11111111.00000000"))