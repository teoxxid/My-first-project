def display_menu():
    """Выводит меню доступных операций."""
    print("\nДобро пожаловать в калькулятор!")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход")

def get_numbers():
    """Запрашивает у пользователя два числа и возвращает их."""
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1, num2
    except ValueError:
        print("Ошибка: введите числа корректно!")
        return None, None

def perform_operation(choice, num1, num2):
    """Выполняет математическую операцию в зависимости от выбора."""
    operations = {
        '1': (lambda a, b: a + b, "+"),
        '2': (lambda a, b: a - b, "-"),
        '3': (lambda a, b: a * b, "*"),
        '4': (lambda a, b: a / b if b != 0 else None, "/")
    }
    
    operation, symbol = operations.get(choice, (None, None))
    
    if operation is None:
        return False
    
    if choice == '4' and num2 == 0:
        print("Ошибка: деление на ноль!")
        return True
    
    result = operation(num1, num2)
    print(f"Результат: {num1} {symbol} {num2} = {result}")
    return True

def calculator():
    """Основная функция калькулятора."""
    while True:
        display_menu()
        choice = input("Выберите операцию (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("Выход из калькулятора. До свидания!")
            break
        
        if choice not in {'1', '2', '3', '4'}:
            print("Ошибка: неверный выбор операции!")
            continue
        
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue
        
        if not perform_operation(choice, num1, num2):
            print("Ошибка: неизвестная операция!")

if __name__ == "__main__":
    calculator()