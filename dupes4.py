def dupes(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
print(dupes([1, 2, 2, 3, 4, 4, 5]))
