def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход")

    while True:
        choice = input("Выберите операцию (1/2/3/4/5): ")

        if choice == '5':
            print("Выход из калькулятора. До свидания!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Ошибка: неверный выбор операции!")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числа корректно!")
            continue

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
            else:
                print(f"Результат: {num1} / {num2} = {num1 / num2}")

if __name__ == "__main__":
    calculator()