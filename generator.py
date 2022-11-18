import random
import string

def prepare_password(password, length):

    password = list(set(password))
    random.shuffle(password)
    password = ''.join(password)
    return str(password[:length])


class password_generator:

    password = ''

    def __init__(self, length, upper_and_lower = None, num_and_let = None, special_sign = None):
        self.length = length
        self.upper_and_lower = upper_and_lower
        self.num_and_let = num_and_let
        self.special_sign = special_sign
        self.create()

    def create(self):
        if (self.upper_and_lower):
            password_generator.password = password_generator.password.join(random.choices(string.ascii_letters, k=self.length))
        else:
            password_generator.password = password_generator.password.join(
                random.choices(string.ascii_lowercase, k=self.length))
        if (self.num_and_let):
            password_generator.password = password_generator.password.join(random.choices(string.digits, k=self.length))
        if (self.special_sign):
            password_generator.password = password_generator.password.join(random.choices(string.punctuation, k=self.length))
        password_generator.password = prepare_password(password_generator.password, self.length)

    def reset(self):
        password_generator.password = ''

    def __str__(self):
        return password_generator.password




