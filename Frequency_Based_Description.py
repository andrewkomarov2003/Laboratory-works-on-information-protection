import sys
import math

# frequency list:
frequency = {0: 8.08, 1: 1.67, 2: 3.18, 3: 3.99, 4: 12.56, 5: 2.17, 6: 1.8, 7: 5.27, 8: 7.24, 9: 0.14, 10: 0.63,
             11: 4.04, 12: 2.6, 13: 7.38, 14: 7.47, 15: 1.91, 16: 0.09, 17: 6.42, 18: 6.59, 19: 9.15, 20: 2.79, 21: 1,
             22: 1.89, 23: 0.21, 24: 1.65, 25: 0.07}

encrypted_message = input()

decrypted_message = ""

min_probability = sys.maxsize

# decrypting:
for symbol in range(26):
    message = [""] * len(encrypted_message)

    # shift:
    for index, curr_symbol in enumerate(encrypted_message):
        if curr_symbol.isalpha():
            sym_num = ord('a') if curr_symbol.islower() else ord('A')
            current_s = (ord(curr_symbol) - sym_num + symbol) % 26
            message[index] = chr(current_s + sym_num)
        else:
            message[index] = curr_symbol

    caesar_text = "".join(message)

    # probability calculation:
    start_sym = ord('a')
    freq = [0] * 26
    curr_caesar_text = caesar_text.lower()
    for sym_caesar in curr_caesar_text:
        curr_sym_caesar = ord(sym_caesar) - start_sym
        if 0 <= curr_sym_caesar <= 25:
            freq[curr_sym_caesar] += 1
    size = len(curr_caesar_text)
    count = 0
    for freq_val in range(26):
        diff = (freq[freq_val] / size) * 100
        count += (frequency[freq_val] - diff) ** 2
    probability = math.sqrt(count)

    if probability < min_probability:
        min_probability = probability
        decrypted_message = caesar_text

print(decrypted_message)
