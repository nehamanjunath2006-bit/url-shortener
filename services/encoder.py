import string

BASE62 = string.ascii_letters + string.digits

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62[0]
    
    base = len(BASE62)
    arr = []
    while num:
        num, rem = divmod(num, base)
        arr.append(BASE62[rem])
    return ''.join(arr[::-1])