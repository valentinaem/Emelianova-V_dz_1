# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

numbers = [i for i in range (1, 101)]
for i in numbers:
    remaind = i % 10
    integer = i // 10
    if integer == 1:
        print(i, 'процентов')
    elif remaind == 1:
        print(i, 'процент')
    elif remaind == 2 or remaind == 3 or remaind == 4:
        print(i, 'процента')
    else:
        print(i, 'процентов')

