import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()
W = "time."


def my_method(S, W):
    result = []
    iter = 0
    m = 0  # in S
    m_start = 0
    i = 0  # in W
    while m < len(S):
        iter += 1
        if S[m] == W[i]:
            if i == len(W) - 1:
                result.append(m_start)
                m_start += 1
                m = m_start
                i = 0
            else:
                m += 1
                i += 1
        else:
            m_start += 1
            m = m_start
            i = 0
    return result, iter


t_start = time.perf_counter()
res = my_method(S, W)
t_stop = time.perf_counter()
print(f"{len(res[0])}; {res[1]}")
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def Rabin_Karp(S, W):
    result = []
    iter = 0
    d = 256
    q = 101  # liczba pierwsza

    def hash(word):
        hw = 0
        for i in range(len(W)):  # N - to długość wzorca
            hw = (hw * d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
        return hw

    hW = hash(W)
    for m in range(len(S) - len(W) + 1):
        hS = hash(S[m:m+len(W)])
        iter += 1
        if hS == hW:
            if S[m:m+len(W)] == W:
                result.append(m)
    return result, iter


t_start = time.perf_counter()
res = Rabin_Karp(S, W)
t_stop = time.perf_counter()
#print(f"{len(res[0])}; {res[1]}")
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def Rabin_Karp_rolling(S, W):
    M = len(S)
    N = len(W)
    result = []
    iter = 0
    diff_string = 0
    d = 256
    q = 101  # liczba pierwsza
    h = 1
    for i in range(N - 1):  # N - jak wyżej - długość wzorca
        h = (h * d) % q

    def hash(word):
        hw = 0
        for i in range(N):  # N - to długość wzorca
            hw = (hw * d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
        return hw

    hW = hash(W)
    for m in range(M - N + 1):
        if m == 0:
            hS = hash(S[m:m+N])
        else:
            hS = (d * (hS - ord(S[m-1]) * h) + ord(S[m + N - 1])) % q
            if hS < 0:
                hs += q
        iter += 1
        if hS == hW:
            if S[m:m+N] == W:
                result.append(m)
            else:
                diff_string += 1
    return result, iter, diff_string


t_start = time.perf_counter()
res = Rabin_Karp_rolling(S, W)
t_stop = time.perf_counter()
print(f"{len(res[0])}; {res[1]}; {res[2]}")
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def KMP(S, W):
    m = 0
    i = 0
    comparisons = 0
    T = KMP_table(W)

    P = []
    nP = 0
    while m < len(S):
        comparisons += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m-i)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return nP, comparisons, T


def KMP_table(W):
    pos = 1
    cnd = 0
    T = []

    T.append(-1)
    while pos < len(W):
        if W[pos] == W[cnd]:
            T.append(T[cnd])
        else:
            T.append(cnd)
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T.append(cnd)
    return T


t_start = time.perf_counter()
res = KMP(S, W)
t_stop = time.perf_counter()
print(f"{res[0]}; {res[1]}; {res[2]}")
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))




