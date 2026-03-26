from services.cache import get_url, set_url
from services.db import fetch_url, conn
import datetime


def redirect(short_code, ip, user_agent):

    # 1️⃣ Check cache
    url = get_url(short_code)
    if url:
        return url

   # 2 Check database
    original_url = fetch_url(short_code)

    if not original_url:
      return None

    # 3️⃣ Save in cache
    set_url(short_code, original_url)
    cur = conn.cursor()
    # 4️⃣ Save analytics
    cur.execute(
        """
        INSERT INTO analytics (short_code, ip_address, user_agent, clicked_at)
        VALUES (%s, %s, %s, %s)
        """,
        (short_code, ip, user_agent, datetime.datetime.utcnow())
    )

    conn.commit()
    cur.close()
    conn.close()

    return original_url