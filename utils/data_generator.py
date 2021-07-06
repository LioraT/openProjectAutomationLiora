import configparser
import string
import random


class DataGenerator:

    @staticmethod
    def random_generator(size=10, chars=string.digits):
        return ''.join(random.choice(chars) for i in range(size))
