    #Задание 6
#while True:
probeg_a = int(input("Введите пробег в 1й день: "))
probeg_b = int(input("Введите пробег в искомый день: "))
i = 1
while probeg_a <= probeg_b:
    probeg_a = 1.1 * probeg_a
    #print(probeg_a) - выводим пробег каждого дня
    i += 1
print(f"Результат тренировок в {probeg_b} км будет достигнут на {i} день")