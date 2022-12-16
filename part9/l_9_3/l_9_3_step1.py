s = 'foO BaR BAZ quX'
'''
Метод capitalize() возвращает копию строки, 
в которой первая буква имеет верхний регистр, 
а все остальные буквы имеют нижний регистр.
'''
print(s.capitalize())  # returns  Foo bar baz qux
s = 'foo123#BAR#.'
print(s.capitalize())  # not affect special characters - Foo123#bar#.


'''
Метод lower() возращает копию строки, в которой все символы имеют нижний регистр.
'''
s = 'i LEARN Python LAnguaGE'
print(s.lower())

'''
Метод upper() возвращает копию строки, в которой все символы имеют верхний регистр.
'''
s = 'i LEARN Python LAnguaGE'
print(s.upper())

'''
Метод swapcase() возвращает копию строки, 
в которой все символы имеющие верхний регистр преобразуются в нижний регистр и наоборот.
'''
s = 'i LEARN Python LAnguaGE'
print(s.swapcase())
