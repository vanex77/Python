    # Задание 5
#while True:
    doxod = int(input("Введите месячный доход фирмы: "))
    rasxod = int(input("Введите месячные расходы фирмы: "))
    if doxod > rasxod:
        print("Прибыль составила: ", doxod - rasxod, ". Рентабельность: ", (doxod - rasxod)/doxod)
        state = int(input("Введите число сотрудников: "))
        print("Прибыль на одного сотрудника составила: ", (doxod - rasxod)/state)
    if doxod < rasxod:
        print("Убытки составили: ", rasxod - doxod)
    if doxod == rasxod:
        print("Фирма сработатла в ноль")