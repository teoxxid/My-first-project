import cmath
import math

def calculator():
    print("\n" + "="*40)
    print(" "*10 + "КАЛЬКУЛЯТОР 2.0 (с комплексными числами)")
    print("="*40)
    print("\nДоступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (√)")
    print("7. Тригонометрическая форма")
    print("8. Выход\n")

    history = []

    def parse_complex(input_str):
        try:
            return complex(input_str.replace('i', 'j'))
        except ValueError:
            try:
                return float(input_str)
            except ValueError:
                raise ValueError("Некорректный ввод числа")

    while True:
        choice = input("Выберите операцию (1-8): ").strip()

        if choice == '8':
            print("\nИстория операций:")
            for op in history:
                print(op)
            print("\nВыход из калькулятора. До свидания!")
            break

        if choice not in ('1', '2', '3', '4', '5', '6', '7'):
            print("Ошибка: неверный выбор операции!")
            continue

        try:
            if choice != '6' and choice != '7':
                num1 = parse_complex(input("Введите первое число (например: 3+2i): "))
                num2 = parse_complex(input("Введите второе число (например: 1-4i): "))
            elif choice == '6':
                num1 = parse_complex(input("Введите число (например: 3+2i): "))
                num2 = None
            elif choice == '7':
                num1 = parse_complex(input("Введите комплексное число (например: 1+1i): "))
                num2 = None
        except ValueError as e:
            print(f"Ошибка: {e}")
            continue

        result = None
        operation = ""
        
        if choice == '1':
            result = num1 + num2
            operation = f"({num1}) + ({num2}) = {result}"
        elif choice == '2':
            result = num1 - num2
            operation = f"({num1}) - ({num2}) = {result}"
        elif choice == '3':
            result = num1 * num2
            operation = f"({num1}) * ({num2}) = {result}"
        elif choice == '4':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = num1 / num2
            operation = f"({num1}) / ({num2}) = {result}"
        elif choice == '5':
            result = num1 ** num2
            operation = f"({num1}) ^ ({num2}) = {result}"
        elif choice == '6':
            result = cmath.sqrt(num1)
            operation = f"√({num1}) = {result}"
        elif choice == '7':
            r = abs(num1)
            phi = cmath.phase(num1)
            operation = f"Тригонометрическая форма: {r}*(cos({phi}) + i*sin({phi}))"

        history.append(operation)
        print("\n" + "="*40)
        print(f"Результат: {operation}")
        print("="*40 + "\n")

if __name__ == "__main__":
    calculator()