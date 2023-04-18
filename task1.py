import datetime
import random

day = datetime.date.today().strftime("%d")
month = datetime.date.today().strftime("%m")
temperature = random.randint(-20, 30)

print(f"Сегодня {day}.{month}. На улице {temperature} градусов.")

if temperature < 0:
    print("Холодно, лучше остаться дома.")