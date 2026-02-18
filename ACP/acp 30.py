import random
import string

chars= string.ascii_letters + string.digits + string.punctuation

password=''.join(random.choice(chars) for i in range(7))
print(password)