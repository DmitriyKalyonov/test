print('Привет! Я простенький калькулятор!\n')
answer = 'да'

while answer == 'да':
    print('КАЛЬКУЛЯТОР')
    print('========================================================')
    while True:
        command = input("Выберите операцию: ")
        if command in "+-*/":
            break
        print("Ошибка: операция не предусмотрена. Попробуйте ещё раз.")

    count = 1
    n = int(input(f"Введите число операндов: "))
    number = int(input(f"Введите число {count}: "))
    result_str = str(number)
    result = number
    while n > 1:
        n -= 1
        count += 1
        number = int(input(f"Введите число {count}: "))

        if number != 0:
            if command == "+":
                result += number
            elif command == "-":
                result -= number
            elif command == "*":
                result *= number
            elif command == "/":
                result /= number
        result_str += " " + command + " " + str(number)

    print(result_str + " = " + str(result))

    print()
    answer = input('Нужно что-то ещё посчитать? (да/нет): ')
