number_lines = input()
number_lines = int(number_lines[1:])
results = []
for i in range(number_lines):
    line = input()
    if '#' in line:
        line = line[:line.index('#')]
    results.append(line.rstrip())

print(*results, sep='\n')

'''
n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())
'''