"""
Чистые функции (Pure Functions):
Они не изменяют состояние программы или внешние переменные.
"""
def add(a, b):
    return a + b

result = add(3, 4)  # В результате нет побочных эффектов


"""
Неизменяемость (Immutable Data): 
после создания объекта его нельзя изменить. 
Вместо этого создается новый объект с измененным состоянием.
"""
# Создание нового списка с измененным элементом
original_list = [1, 2, 3]
new_list = [x * 2 for x in original_list]  # Не изменяет оригинальный список


"""
Функции высших порядков (Higher-Order Functions): 
Это функции, которые принимают другие функции в качестве аргументов 
или возвращают их в качестве результатов.
"""
def apply(func, x):
    return func(x)

def square(x):
    return x ** 2

result = apply(square, 5)  # Применение функции square через функцию apply


"""
Рекурсия: Функциональное программирование активно использует рекурсию для решения задач.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)  # Вычисление факториала через рекурсию


"""
Функции первого класса (First-Class Functions): 
Функции рассматриваются как обычные значения и могут быть присвоены переменным, 
переданы как аргументы и возвращены из других функций.
"""
# Функция, которая принимает функцию как аргумент
def apply(func, x):
    return func(x)

# Обычная функция, которая возводит число в квадрат
def square(x):
    return x ** 2

# Функция, которая возводит число в куб
def cube(x):
    return x ** 3

# Присвоение функций переменным
my_function1 = square
my_function2 = cube

# Использование функций как аргументов
result1 = apply(my_function1, 5)  # Вызов apply с функцией square
result2 = apply(my_function2, 3)  # Вызов apply с функцией cube

print(result1)  # Вывод: 25 (5 в квадрате)
print(result2)  # Вывод: 27 (3 в кубе)


"""
Лямбда-функции: Лямбда-функции (анонимные функции) позволяют создавать короткие и одноразовые функции без явного определения имени функции.
"""
def add(x, y):
    return x + y

add = lambda x, y: x + y  # Лямбда-функция для сложения двух чисел
result = add(3, 4)  # Вызов лямбда-функции








squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Вывод: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]


# Создание множества, содержащего квадраты чисел от 1 до 5
squares_set = {x ** 2 for x in range(1, 6)}
print(squares_set)  # Вывод: {1, 4, 9, 16, 25}


# Создание словаря, где ключами являются числа от 1 до 5, а значениями - их квадраты
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)  # Вывод: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Генерация списка списков с числами от 1 до 3 в каждом внутреннем списке
matrix = [[x for x in range(1, 4)] for _ in range(3)]
print(matrix)
# [
#   [1, 2, 3],
#   [1, 2, 3],
#   [1, 2, 3]
# ]


from functools import reduce

# Список студентов с баллами
students = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 78},
]

# Используем reduce для суммирования баллов студентов
total_score = reduce(lambda x, y: x + y["score"], students, 0)

print("Общий суммарный балл всех студентов:", total_score)