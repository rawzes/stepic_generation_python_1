s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))
print(s.replace('foo', 'grault', 2))


s = '     foo bar foo baz foo qux      '
print(s.strip())
print(s.lstrip())
print(s.rstrip())



s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 7))


s = 'foobar'
print(s.startswith('foo', 0, 3))
print(s.startswith('baz'))

s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))


s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))

'''
Метод rfind(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), 
за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки s.
'''

print(s.rfind('qux'))
print(s.rfind('qux', 19, 19))  # -1

'''
Метод index(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), 
за тем исключением, что он вызывает ошибку  
ValueError: substring not found во время выполнения программы, 
если подстрока <sub> не найдена.
'''

print(s.index('test'))  # ValueError: substring not found


