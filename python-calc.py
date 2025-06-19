def calculator():
    print("\n" + "="*40)
    print(" "*10 + "КАЛЬКУЛЯТОР 2.0")
    print("="*40)
    print("\nДоступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (√)")
    print("7. Выход\n")

    history = []  

    while True:
        choice = input("Выберите операцию (1-7): ").strip()

        if choice == '7':
            print("\nИстория операций:")
            for op in history:
                print(op)
            print("\nВыход из калькулятора. До свидания!")
            break

        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Ошибка: неверный выбор операции!")
            continue

        try:
            if choice != '6':  
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            else:
                num1 = float(input("Введите число: "))
                num2 = None  
        except ValueError:
            print("Ошибка: введите число корректно!")
            continue

        result = None
        operation = ""
        
        if choice == '1':
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"
        elif choice == '4':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = num1 / num2
            operation = f"{num1} / {num2} = {result}"
        elif choice == '5':
            result = num1 ** num2
            operation = f"{num1} ^ {num2} = {result}"
        elif choice == '6':
            if num1 < 0:
                print("Ошибка: нельзя извлечь корень из отрицательного числа!")
                continue
            result = num1 ** 0.5
            operation = f"√{num1} = {result}"

        history.append(operation)  
        print("\n" + "="*40)
        print(f"Результат: {operation}")
        print("="*40 + "\n")

if __name__ == "__main__":
    calculator()