palindromes = [v for v in range(100, 1000) if str(v)[0] == str(v)[2]]
print(palindromes)

# or

palindromes = [v for v in range(100, 1000) if str(v) == str(v)[::-1]]
print(palindromes)
