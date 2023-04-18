def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input("Введите n: "))
value = fib(n)
print(f"Значение числа Фибоначчи под номером {n} равно {value}")
