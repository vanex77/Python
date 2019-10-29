    #Задание 2
num_sec = int(input("Введите количество секунд: "))
hours = num_sec // 3600
minutes = num_sec % 3600 // 60
seconds = num_sec % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# Задание 2.1
#while True:
#    num_sec = int(input("Введите количество секунд: "))
#    hours = str(num_sec // 3600)
#    minutes = str(num_sec % 3600 // 60)
#    seconds = str(num_sec % 60)
#    if num_sec // 3600 < 10:
#        hours = "0" + hour
#    if num_sec % 3600 // 60 < 10:
#        minutes = "0" + minutes
#    if num_sec % 60 < 10:
#        seconds = "0" + seconds
#    print("%s:%s:%s" % (hours, minutes, seconds))
#    #print("{}:{}:{}".format(hours, minutes, seconds))
#    #print(f"{hours}:{minutes}:{seconds}")

    # Задание 2.2
#while True:
#    num_sec = int(input("Введите количество секунд: "))
#    print("%2d:%2d:%2d" % (num_sec // 3600, num_sec % 3600 // 60, num_sec % 60))