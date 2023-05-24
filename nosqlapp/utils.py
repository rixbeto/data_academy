import random
import string


class Mok():

    def __init__(self):
        self.ar = None

    def random_string(self,length = 10):
        characters = string.ascii_letters
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def random_bool(self):
        return random.choice([0, 1])

    def random_periodicity(self):
        return random.choice(["daily", "weekly", "monthly", "once_at_week", "once_at_month"])


