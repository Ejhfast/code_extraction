# PHP SHA-512 to Python+C SHA-512
import crypt
def hashPassword(salt, password, rounds=5000):
    return crypt.crypt(password, '$6$rounds={:d}${}$'.format(rounds, salt))
