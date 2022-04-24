time = int(input('Введите целое число: '))
print('В числе cодержится: ')
days = time // 86400
if days > 0:
    print(days, 'дн.')
hours = (time % 86400) // 3600
if hours > 0:
    print(hours, 'ч.')
min = ((time % 86400) % 3600) // 60
if min > 0:
    print(min, 'мин.')
sec = ((((time % 86400) % 3600) % 60) // 1)
if sec > 0:
    print(sec, 'сек.')