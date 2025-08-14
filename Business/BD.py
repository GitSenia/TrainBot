import os
import psycopg2
from Config.DBconfig import conect as c
import os
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "Config", "T.txt")
file_path = os.path.abspath(file_path)# Превращаем в абсолютный путь

#функция заполняет базу данных станциями Беларуси
def insert():
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
    conn = psycopg2.connect(
        host=c['host'],
        database=c['database'],
        user=c['user'],
        port=c['port'],
        password=c['password'],
    )
    cur = conn.cursor()
    for line in lines:
        if line.strip():
            cur.execute("INSERT INTO stations (name_station) VALUES (%s)", (line.strip(),))
    conn.commit()
    cur.close()
    conn.close()

