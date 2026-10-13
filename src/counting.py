
def count_accepted(delta, accepting, n):
    num_states = len(delta)
    num_symbols = len(delta[0])

    prev = [1 if f else 0 for f in accepting]
    for i in range(n):
        curr = [0] * num_states
        for q in range(num_states):
            for a in range(num_symbols):
                curr[q] += prev[delta[q][a]]
        prev = curr
    return prev[0]