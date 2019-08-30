# Поисковый радиус для определения границ поиска оптимального числа
SearchRadius = 0.1
# Ввод текстовой строки для последующего превращения в код BrainF***
text_string = input("Enter some text string.")
# Строка вывода кода
bf_code = ""
# Объявление переменной для хранения среднего значения номеров символов по ASCII таблице
avg = 0
# Перебор всех символов в строке и последующее нахождение среднего значения
for charect in text_string:
    avg += ord(charect)
avg //= len(text_string)
# Объявление пенременных для поиска оптимальных множителей
a, b = 1, avg
# Перебор всех значений, находящихся в радиусе поиска (10% от среднего) для поиска оптимального значения
# На каждой итерации перебираются возможные делители исследуемого числа
# Определение оптимальности производится путём расёта цены
# Цена равна сумме множителей и остатка от разности оптимального числа (модуль разности произведение оптимальных множителей и среднего числа)
for i in range(avg - int(avg * SearchRadius), avg + int(avg * SearchRadius) + 1):
    for j in range(1, i // 2 + 1):
        if(i % j == 0) and (i // j + j + abs(avg - i) < a + b + abs(avg - a * b)):
            a, b = i//j, j
print("Average: {0}, Optimal Nearest: {1}, Optimal Multipliers: {2} {3}, Cost: {4}".format(avg, a * b, a, b, a+b+abs(avg - a * b)))
# Сборка строки кода в зависимости от длины введённой пользователем строки
if(len(text_string)>1):
    bf_code = '+' * a + "[>" + '+' * b + "<-]" + ">[" + ">+" * len(text_string) + "<" * len(text_string)+"-]"
    for charect in text_string:
        if(ord(charect) - avg > 0):
            bf_code += '>' + '+'*(ord(charect) - a*b) + '.'
        else:
            bf_code = '+' * a + "[>" + '+' * b + "<-]" + ">[" + ">+" * len(text_string) + "<" * len(text_string) + "-]"
else:
    bf_code = '+' * a + "[>" + '+' * b + "<-]>."
print(bf_code)