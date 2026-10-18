from buffers import *

def crossed(left, right):
    k = len(left)
    for i in range(5):
        j = 4 - i
        if i <= k and j <= k:
            window = []
            for t in range(i):
                window.append(left[t])
            window.append(0)
            for t in range(j):
                window.append(right[t])
            if mask(window) != ALL_LETTERS:
                return False
    return True


def build_dfa_L2(delta_L):
    S = NUM_STATES_L
    FAIL = 1

    a = encode([0])
    start_code = a * S + a

    state_of = {}
    state_of[start_code] = 0

    codes = []
    codes.append(start_code)
    codes.append(-1)

    delta = []

    s = 0
    while s < len(codes):
        if s == FAIL:
            row = []
            for c in range(16):
                row.append(FAIL)
            delta.append(row)
            s += 1
            continue
        p = codes[s] // S
        q = codes[s] % S
        left_buf = decode(p)
        right_buf = decode(q)

        need_cross = False
        if len(left_buf) >= 2 and len(left_buf) <= 4:
            need_cross = True

        row = []
        for x in range(4):
            temp_p = delta_L[p][x]
            for y in range(4):
                temp_q = delta_L[q][y]
                if temp_p == FAIL_L or temp_q == FAIL_L:
                    row.append(FAIL)
                    continue
                if need_cross:
                    left = []
                    for t in range(1, len(left_buf)):
                        left.append(left_buf[t])
                    left.append(x)

                    right = []
                    for t in range(1, len(right_buf)):
                        right.append(right_buf[t])
                    right.append(y)
                    if not crossed(left, right):
                        row.append(FAIL)
                        continue

                temp_code = temp_p * S + temp_q
                if temp_code not in state_of:
                    state_of[temp_code] = len(codes)
                    codes.append(temp_code)
                row.append(state_of[temp_code])
        delta.append(row)
        s += 1

    accept = []
    for i in range(len(codes)):
        if i == FAIL:
            accept.append(False)
        else:
            accept.append(True)
    return delta, accept