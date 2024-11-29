import hashlib
import itertools
def crack(hash):
    current_cracked = hashlib.md5('00078'.encode())
    for combination in itertools.product(range(10), repeat=5):
        combination = ''.join(list(map(str, combination)))
        current_cracked = hashlib.md5(combination.encode()).hexdigest()

        if current_cracked == hash:
            return combination
