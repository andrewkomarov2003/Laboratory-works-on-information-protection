def dis_log(G, H, Q):
    for x in range(1, Q):
        if pow(G, x, Q) == H:
            return x
    return None

G, H, Q = map(int, input().strip().split())

X = dis_log(G, H, Q)

print(X)
