SIGMA = 4
BUF_MAX = 5
ALL_LETTERS = 0b1111

OFFSET = [(SIGMA ** K - 1) // 3 for K in range(BUF_MAX + 2)]
NUM_BUFFERS = OFFSET[BUF_MAX + 1]
FAIL_L = NUM_BUFFERS
NUM_STATES_L = NUM_BUFFERS + 1

def encode(buffers):
    # Puts buffer list into base 4 number
    val = 0
    for s in buffers:
        val = val * SIGMA + int(s)
    #offset so [a] and [a][a] are different
    return OFFSET[len(buffers)] + val

def decode(q):
    #inverse of encode
    k = 0
    while OFFSET[k + 1] <= q:
        k += 1
    value = q - OFFSET[k]
    buffers = []
    for i in range(k):
        buffers.append(value % 4)
        value //= 4
    #last char first so reverse
    buffers.reverse()
    return buffers

def mask(symbols):
    # Returns which letters are present
    # [a,c,a] gives 0b0101
    m = 0
    for s in symbols:
        m |= 1 << s
    return m
        

