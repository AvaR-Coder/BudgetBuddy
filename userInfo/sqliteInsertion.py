username = ""
email = ""
 = ""
cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", (username, email, password_hash))
    conn.commit()
