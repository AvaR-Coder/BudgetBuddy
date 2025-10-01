import re
from argon2 import PasswordHasher

def checkPasswordStrength(password):

  if len(password) < 8:
    print("Password needs to be at 8 characters long.")
    return False
    
  if not re.search(r"[A-Z]", password):
    print("Password needs at least one uppercase letter.")
    return False

  if not re.search(r"[a-z]", password):
    print("Password needs at least one lowercase letter.")
    return False

  if not re.search(r"\d", password):
    print("Password needs at least one number.")
    return False

  if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
    print("Password needs at least one special character.")
    return False
  
  return True

def hashThePassword(password):
  
  ph = PasswordHasher(time_cost=2, memory_cost=102400, parallelism=8, salt_len=16, hash_len=32)
  hashed_password = ph.hash(password)
  
