cache = {}

def get_url(short_code):
    return cache.get(short_code)

def set_url(short_code, long_url, ttl=86400):
    cache[short_code] = long_url