#Ввод последовательности чисел
user_input_seq = input("Введите целые числа через пробел: ")
user_input = int(input("Введите целое число: "))    #Ввод числа пользователя
#Проверка на наличие пробелов
if " " not in user_input_seq:
        print("Ошибка! Необходимо ввести числа через пробел. "
              "Перезапустите программу.")
#Приведение последовательности к списку
sequence = [int(i) for i in user_input_seq.split()]

#Cортировка списка по возрастанию
def sorted_list(sequence, left, right):
    middle = sequence[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while sequence[i] < middle:
            i += 1
        while sequence[j] > middle:
            j -= 1
        if i <= j:
            sequence[i], sequence[j] = sequence[j], sequence[i]
            i += 1
            j -= 1
    if j > left:
        sorted_list(sequence, left, j)
    if right > i:
        sorted_list(sequence, i, right)

#Установка введённого пользователем элемента
def binary_search(sequence, user_input, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if sequence[middle] == user_input:
        return middle
    elif user_input < sequence[middle]:
        return binary_search(sequence, user_input, left, middle - 1)
    else:
        return binary_search(sequence, user_input, middle + 1, right)

sequence.append(user_input)
sorted_list(sequence, 0, len(sequence)-1)
binary_search(sequence, user_input, 0, len(sequence))

print(f'Индекс вашего числа в отсортированной последовательности: '
      f'{binary_search(sequence, user_input, 0, len(sequence))}')
