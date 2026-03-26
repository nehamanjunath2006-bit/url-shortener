from services.db import conn
from datetime import datetime

def log_click(short_code, ip, user_agent):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO analytics (short_code, ip_address, user_agent, clicked_at)
        VALUES (%s, %s, %s, %s);
    """, (short_code, ip, user_agent, datetime.utcnow()))
    conn.commit()


def get_analytics(short_code):
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            COUNT(*) as total_clicks
        FROM analytics
        WHERE short_code = %s;
    """, (short_code,))
    
    total_clicks = cur.fetchone()[0]

    cur.execute("""
        SELECT DATE(clicked_at) as day, COUNT(*) 
        FROM analytics
        WHERE short_code = %s
        GROUP BY day
        ORDER BY day;
    """, (short_code,))
    
    time_stats = cur.fetchall()

    return {
        "short_code": short_code,
        "total_clicks": total_clicks,
        "time_stats": time_stats
    }
