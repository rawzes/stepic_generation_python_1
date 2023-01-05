s = input().lower().split()

articles = ['a', 'an', 'the']
total_count = 0

for article in articles:
    total_count += s.count(article)

print(f'Общее количество артиклей: {total_count}')

