# xor function:
def xor(a, b):
    decrypted_message = ''
    for i in range(len(a)):
        decrypted_message += hex(int(a[i], 16) ^ int(b[i], 16))[2:]
    return decrypted_message


# Alice and Bob messages:
a = input()
b = input()
c = input()

# decrypting:
decrypted_message = xor(xor(a, b), c)

output = ''.join(chr(int(decrypted_message[i:i + 2], 16)) for i in range(0, len(decrypted_message), 2))

print(output)
