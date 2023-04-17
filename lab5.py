from transliterate import translit

n = int(input())
phone_book = {}
for i in range(n):
    name, phone = input().split()
    phone_book[name] = phone
query = input()
if query in phone_book:
    print(phone_book[query])
else:
    print("Нет в телефонной книге!")

print()

word = input()
d = {}
for letter in word:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1
print(d)

print()

text = input()
result = translit(text, 'ru', reversed=True)
print(result)