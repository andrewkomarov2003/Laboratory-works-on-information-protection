import numpy

def scanner(qrcode):
    values_QR = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(21)]
    for a, line in enumerate(qrcode):
        for b, symbol in enumerate(line):
            if (a + b) % 2 == 0:
                symbol = 1 - symbol
            values_QR[a][b] = symbol
    data_QR = numpy.array(values_QR)
    data_QR = data_QR[9:]
    code = 0
    res = []
    for a in [19, 17, 15, 13]:
        stovp = data_QR[:, [a, a + 1]]
        if code == 1:
            move_dir = 1
        else:
            move_dir = -1

        for line in stovp[::move_dir]:
            res += line.tolist()[::-1]
        code = 1 - code
    res = ''.join(list(map(str, res[4:])))
    out = int(res[:8], 2)
    res = res[8:]
    decode = ''
    print(out)
    for a in range(0, (out * 8) + 11, 8):
        decode += chr(int(res[a:a + 8], 2))
        if len(decode) == out:
            return decode
