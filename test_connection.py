import psycopg2
from config import Config

try:
    conn = psycopg2.connect(
        host="pg-bb42dc0-niranjanmaurya03-4523.l.aivencloud.com",
        port=17692,
        database="tech_news",
        user="avnadmin",
        password="AVNS_99P097r_o42YMQqBksy",
        sslmode="require",
        sslrootcert="ca.pem"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print("✅ Connection successful:", cursor.fetchone()[0])
except Exception as e:
    print("❌ Connection failed:", e)
finally:
    conn.close() if 'conn' in locals() else None