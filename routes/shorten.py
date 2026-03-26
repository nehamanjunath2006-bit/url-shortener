from services.encoder import encode_base62
from services.db import insert_url
from services.cache import set_url

def create_short_url(long_url):
    url_id = insert_url(long_url)   # auto-increment ID
    short_code = encode_base62(url_id)
    
    set_url(short_code, long_url)   # cache
    return short_code