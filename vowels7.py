def vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')
s=str(input())
print(vowels(s))
