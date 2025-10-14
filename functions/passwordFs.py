import re
from argon2 import PasswordHasher

def checkPasswordStrength(password):

  if len(password) < 8:
    return "Password needs to be at 8 characters long."
  if not re.search(r"[A-Z]", password):
    return "Password needs at least one uppercase letter."
  if not re.search(r"[a-z]", password):
    return "Password needs at least one lowercase letter."
  if not re.search(r"\d", password):
    return "Password needs at least one number."
  if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
    return "Password needs at least one special character."
  return None

def hashThePassword(password):
  
  ph = PasswordHasher(time_cost=2, memory_cost=102400, parallelism=8, salt_len=16, hash_len=32)
  hashed_password = ph.hash(password)
  return hashed_password

def getLoginData
  conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
    user = cursor.fetchone()
    return user
  except Exception as e: #No existing user
    return None
  finally:
    conn.close()
