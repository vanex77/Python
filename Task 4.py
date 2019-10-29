    # Задание 4
while True:
    number = input("Введите целое число: ")
    i = 1
    max_digit = int(number[0])
    while i < len(number):
        if int(number[i-1]) < int(number[i]) and max_digit < int(number[i]
            max_digit = int(number[i])
        #elif max_digit < int(number[i]) and max_digit >= int(number[i-1]):
         #   max_digit = int(number[i-1])
        i += 1
    print("Наибольшая цифра в вашем числе: ", max_digit)
