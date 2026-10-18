from buffers import *

def build_dfa_L():
    # delta[q][x] = next state from state q on input letter x
    delta = [[FAIL_L] * SIGMA for i in range(NUM_STATES_L)]
    for q in range(NUM_BUFFERS):
        buf = decode(q)
        for x in range(SIGMA):
            if len(buf) < BUF_MAX:
                #grow buffer
                delta[q][x] = encode(buf + [x])
            
            elif mask(buf + [x]) == ALL_LETTERS:
                #full buffer with all chars found!
                delta[q][x] = encode(buf[1:] + [x])
            
            else:
                #full non accepting buffer. Missing a letter.
                delta[q][x] = FAIL_L
            
    accepting = [q != FAIL_L for q in range(NUM_STATES_L)]
    return delta, accepting
    