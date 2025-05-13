from itertools import product

def horspool_preprocessing(sigma, P, l):
    m = len(P)
    default = m - l + 1

    shifts = { ''.join(chars): default for chars in product(sorted(sigma), repeat=l) }

    for i in range(m - l):
        sub = P[i : i + l]
        shifts[sub] = (m - l) - i

    return shifts


def horspool_search(sigma, P, T, l):
    m, n = len(P), len(T)
    if m > n:
        return [], 0, {}

    shifts = horspool_preprocessing(sigma, P, l)
    default = m - l + 1
    i = m - 1

    matches = []
    comparisons = 0
    shift_counts = {}

    while i < n:
        k = 0
        while k < m:
            comparisons += 1
            if P[m-1-k] != T[i-k]:
                break
            k += 1

        if k == m:
            matches.append(i - m + 1)

        start = i - l + 1
        if start >= 0:
            key = T[start : i+1]
            shift = shifts.get(key, default)
        else:
            shift = default

        shift_counts[shift] = shift_counts.get(shift, 0) + 1
        i += shift

    return matches, comparisons, shift_counts


P     = "ABABBABABA"
T     = "ABAABABABABBABABAABBABABACABBBABABBBABABAABABCBABC"
Sigma = set(P) | set(T)

for l in (1,2,3):
    shifts = horspool_preprocessing(Sigma, P, l)
    print("l=", l, "shifts:", shifts)

    matches, comps, shift_cts = horspool_search(Sigma, P, T, l)
    print("matches:", matches)
    print("comparisons:", comps)
    print("shift_counts:", shift_cts)

