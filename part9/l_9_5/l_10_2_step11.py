s = input()
simbol = 'h'
start_index = s.find(simbol)
end_index = s.rfind(simbol)

result = s[:start_index] + s[end_index:start_index: -1] + s[end_index:]
print(result)
