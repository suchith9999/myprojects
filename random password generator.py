# 1.Method
import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
spacial = string.punctuation
dig = string.digits
gen_up = ''.join((random.choice(upper) for _ in range(1)))
gen_low = ''.join((random.choice(lower) for _ in range(5)))
gen_sp = ''.join((random.choice(spacial) for _ in range(1)))
gen_dig = ''.join((random.choice(dig) for _ in range(1)))
print(gen_up + gen_low + gen_sp + gen_dig)


# 2.Method
class PdRandom:

    def pdrandom(self):
        import random, string
        self.upper = ''.join((random.choice(string.ascii_uppercase) for _ in range(1)))
        self.lower = ''.join((random.choice(string.ascii_lowercase) for _ in range(5)))
        self.special = ''.join((random.choice('!@#$%&*') for _ in range(1)))
        self.digit = ''.join((random.choice(string.digits) for _ in range(1)))
        self.gen = (self.upper + self.lower + self.special + self.digit)
        print(self.gen)


PdRandom().pdrandom()
