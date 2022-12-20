age = 30

text = 'My name is Roma, I am QA. I am ' + str(age)
print(text)

text2 = 'My name is Roma, I am QA. I am {0}'.format(age)
print(text2)

name = 'Roma'
profession = 'QA'
txt = 'My name is {}, I am {}. I work as a {}'.format(name, age, profession)
print(txt)
txt = 'My name is {0}, I am {1}. I work as a {2}'.format(name, age, profession)
print(txt)

print('My name is {0}-{0}-{0}'.format(name))


# лучше всегда использовать f-strings

first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'


print('Hello, {0} {1}. You are {2}. You are a {3}. You were a member of {4}'.
      format(first_name, last_name, age, profession, affiliation))

print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')
