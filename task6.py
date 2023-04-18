num = int(input("Введите простое число: "))

if num < 0:
    print("Ошибка! Введено отрицальное число!")
elif num == 0 or num == 1:
    print("Составное")
else:
    simple_num = True
    for i in range(2, num):
        if num % i == 0:
            simple_num = False
            break
    if simple_num:
        print("Простое")
    else:
        print("Составное")