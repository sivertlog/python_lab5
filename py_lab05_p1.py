def is_valid_part(part):
    """Check individual part of IP address.
    part:Part of IP address as a string
    returns:True or False
    """
    try:
        if part[0] == '0' and len(part) > 1: return False
        return 0 <= int(part) < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    """Check if the IP address is valid.
    ip:IP address as a string
    returns:True or False
    """
    parts=ip.split('.')
    for part in parts:
        if not is_valid_part(part): return False
    return len(parts) == 4

'''
print(is_valid_part("127"),
      is_valid_part("a"),
      is_valid_part("256"),
      is_valid_part("012"),
      is_valid_part("0"),is_valid_part("23"))

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False

'''
