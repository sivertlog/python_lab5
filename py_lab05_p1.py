def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and len(part) > 1: return False
        return 0 <= i_part < 256
    except ValueError as ve:
        return False

def is_valid_ip(ip:str):
    parts=ip.split('.')
    for part in parts:
        if not is_valid_part(part): return False
    return len(parts) == 4

"""
print(is_valid_part("127"),
      is_valid_part("a"),
      is_valid_part("256"),
      is_valid_part("012"),
      is_valid_part("0"),is_valid_part("23"))"""

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False