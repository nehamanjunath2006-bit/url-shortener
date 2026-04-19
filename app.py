from services.db import SessionLocal
from fastapi import FastAPI

app = FastAPI()
@app.post("/shorten")
async def shorten_url(data: dict):
    db = SessionLocal()

    long_url = data.get("long_url")
    short_code = create_short_url(long_url)

    # 🔥 INSERT INTO DATABASE to make sure it gets added - to demo pull
    db.execute(
        """
        INSERT INTO urls (long_url, short_code)
        VALUES (:long, :short)
        """,
        {"long": long_url, "short": short_code}
    )
    db.commit()

    return {"short_url": f"http://localhost:8000/{short_code}"}
