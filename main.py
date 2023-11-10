# Написать в императивном  и декларативном стилях процедуру для
# сортировки числа в списке в порядке убывания.

# Императивный стиль

numbers = [22, 88, 44, 66, 11]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[i]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Отсортированный список в порядке убывания ", numbers)

# Декларативный стиль

numbers = [22, 88, 44, 66, 11]

print("Отсортированный список в порядке убывания ", sorted(numbers, reverse=True))
