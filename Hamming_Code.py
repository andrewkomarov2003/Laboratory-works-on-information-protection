def encode(string):
  bin_data = [-len(bin(ord(value))[2:]) % 8 * '0' + bin(ord(value))[2:] for value in string]
  arr_1 = []
  for binary in bin_data:
    result = "".join(str(element)*3 for element in binary)
    arr_1.append(result)
  return "".join(value for value in arr_1)

def decode(bits):
  bin_data = []
  a = 0
  while a + 2 < len(bits):
    bin = bits[a:a+3]
    cnt_1 = bin.count('1')
    cnt_2 = bin.count('0')
    bin = '1' if cnt_1 > cnt_2 else '0'
    bin_data.append(bin)
    a += 3
  arr_1 = []
  a = 0
  while a + 7 < len(bin_data):
    ACSII = int("".join(x for x in bin_data[a:a+8]), 2)
    b_curr = ACSII.bit_length() + 7 // 8
    arr_2 = ACSII.to_bytes(b_curr, "big")
    ASCII_2 = [x if x != "\x00" else "" for x in arr_2.decode()]
    arr_1.append("".join(value for value in ASCII_2))
    a += 8
  return "".join(value for value in arr_1)
