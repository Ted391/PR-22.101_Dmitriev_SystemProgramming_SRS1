import random as rnd

def Task1():
    print("============== Задание #1 ==============\n")

    randomList = [rnd.randint(1, 100) for i in range(rnd.randint(1, 10))]

    print(f"              Исходный список: {randomList}")

    for i in range(len(randomList)):
        randomList[i] = randomList[i] ** 2

    print(f"Список с квадратами элементов: {randomList}")
    
    print("\n========================================\n\n")

def Task2():
    print("============== Задание #2 ==============\n")

    initialList = [1, 2, 3, 4, 2, 5, 3, 6, 7, 8, 7] # Заданный список
    duplicates = [] # Список повторяющихся элементов

    for number in initialList:
        if initialList.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    print(f"Дубликаты в списке: {duplicates}")

    print("\n========================================\n\n")

def Task3():
    print("============== Задание #3 ==============\n")

    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    unique_elements = [element for element in list2 if element not in list1]

    print("Исходные списки:")
    print(list1)
    print(list2)
    print()
    print(f"Элементы из второго списка, которых нет в первом: {unique_elements}")

    print("\n========================================\n\n")

def Task4():
    print("============== Задание #4 ==============\n")

    numbers = [10, 20, 30, 40, 20, 50]
    print(f"  Исходный массив: {numbers}")

    for i in range(len(numbers)):
        if numbers[i] == 20:
            numbers[i] = 200

    print(f"Изменённый массив: {numbers}")

    print("\n========================================\n\n")

def Task5():
    print("============== Задание #5 ==============\n")

    numbers = [2, 3, 4, 5, 6, 8, 10, 13, 15, 12, 14, 16, 21, 25]
    print(f"Исходный массив: {numbers}\n")

    print("Чётные числа из заданного списка до значения 15:")

    for number in numbers:
        if number == 15:
            break
        if number % 2 == 0:
            print(number)
    
    print("\n========================================\n\n")

    # Вариант 10
def Task6():
    print("============== Задание #6 ==============\n")

    numbers_str = input("Введите целые числа, разделенные пробелами: ")
    numbers = [int(x) for x in numbers_str.split()]

    while len(numbers) < 4:
        numbers_str = input("Некорректные данные! Введите не менее 4 целых чисел, разделенных пробелами: ")
        numbers = [int(x) for x in numbers_str.split()]

    print(f"Исходный список: {numbers}")

    modified_numbers = numbers # Копия

    modified_numbers.remove(min(numbers))
    modified_numbers.remove(max(numbers))

    print(f"Измененный список: {modified_numbers}")

    print("\n========================================\n\n")


    # Run
if __name__ == "__main__":
    Task1()
    Task2()
    Task3()
    Task4()
    Task5()
    Task6()