import py_lab05_p2 as conv

def is_valid_part(part):
    """Check individual part of IP address.
    :param part: Part of IP address as a string
    :return: True or False
    """
    try:
        if part[0] == '0' and len(part) > 1: return False
        return 0 <= int(part) < 256
    except (ValueError, IndexError) as ve_or_ie:
        return False

def is_bin_part(part):
    '''Check individual part of IP address in binary notation
    :param part: Part of IP in binary as a string
    :return: True or False
    '''
    if (part.count('0') + part.count('1') == len(part)): return (len(part) == 8)
    return False

def is_valid_ip(ip:str):
    """Check if the IP address is valid.
    :param ip: IP address as a string
    :return: True or False
    """
    parts=ip.split('.')
    for part in parts:
        if not is_valid_part(part): return False
    return len(parts) == 4

def is_valid_bin_ip(ip:str):
    '''Check if the ip is binary and valid
    :param ip: binary IP address as a string
    :return: True or False
    '''
    parts=ip.split('.')
    for part in parts:
        if (not is_bin_part(part)) or (not is_valid_part(str(conv.binary_to_decimal(part)))):
            return False
    return len(parts) == 4