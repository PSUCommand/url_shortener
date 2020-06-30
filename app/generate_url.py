import random
import string

#метод генерации ссылки
def generate_url(size):
    shortLink = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
    return shortLink