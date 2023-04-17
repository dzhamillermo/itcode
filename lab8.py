import random
import string
import datetime

def generate_passwords(n, k):
    passwords = set()
    while len(passwords) < n:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=k))
        passwords.add(password)
    return passwords

n = int(input("Введите количество паролей: "))
k = int(input("Введите длину пароля: "))

passwords = generate_passwords(n, k)
print(f"{n} различных паролей длинной {k} символов: ")
for password in passwords:
    print(password)

print("-------------------------------")

n = int(input("Введите количество экзаменов: "))

disciplines = input("Введите наименования дисциплин через запятую и пробел: ").split(", ")

days = ["понедельник", "вторник", "среда", "четверг", "пятница"]
exam_days = random.choices(days, k=n)

start_time = datetime.datetime.strptime("09:00", "%H:%M")
end_time = datetime.datetime.strptime("14:00", "%H:%M")
delta = datetime.timedelta(minutes=30)

times = []
while start_time <= end_time:
    times.append(start_time.strftime("%H:%M"))
    start_time += delta

exam_times = random.sample(times, k=n)

ticket_numbers = random.choices(range(1, 21), k=n)

exams = list(zip(exam_days, exam_times, ticket_numbers))
exams.sort(key=lambda x: x[1])

for i in range(n):
    print(f"Экзамен по дисциплине {disciplines[i]} состоится в {exams[i][0]} время {exams[i][1]}. Ваш счастливый билет {exams[i][2]}.")

print("-------------------------------")

K = int(input("Введите количество дней до экзамена: "))
exam_date = datetime.date.today() + datetime.timedelta(days=K)

print(f"Экзамен состоится {exam_date.strftime('%d.%m.%Y')}.")

print("-------------------------------")

date_str = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))

date = datetime.datetime.strptime(date_str, "%Y/%m/%d").date()

dates = []
while len(dates) < 3:
    if date.weekday() != 0 and date.day % 4 != 0:
        dates.append(date)
    date += datetime.timedelta(days=n)

for date in dates:
    print(f"{date.strftime('%d %B')}, {date.strftime('%A')}")