import sqlite3
import hashlib


conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")


username1, password1 = "mike1", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "mike2", hashlib.sha256("mikepassword1".encode()).hexdigest()
username3, password3 = "mike3", hashlib.sha256("mikepassword2".encode()).hexdigest()
username4, password4 = "mike4", hashlib.sha256("mikepassword3".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()