def missed(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)
print(missed([1, 2, 4, 5], 5))
