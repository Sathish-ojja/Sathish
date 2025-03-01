from collections import Counter

def frequent(lst):
    return Counter(lst).most_common(1)[0][0]


print(frequent([1, 2, 3, 1, 2, 1]))
