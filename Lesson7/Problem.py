# Задание-1
# Есть два игрока и 25 монет.
# Каждый может брать от 1 до 3 монет.
# Проигрывает тот кто забрал последнюю.
# Написать программу для этой игры

def pl1_coins() -> int:
    pl1_coins = 0
    while not 1 <= pl1_coins <= 3:
        try:
            pl1_coins = int(input("Игрок1 введите число монет от 1 до 3: "))
        except ValueError:
                print("Неверное значение! Введите цифру от 1 до 3")
    return pl1_coins

def pl2_coins() -> int:
    pl2_coins = 0
    while not 1 <= pl2_coins <= 3:
        try:
            pl2_coins = int(input("Игрок2 введите число монет от 1 до 3: "))
        except ValueError:
                print("Неверное значение! Введите цифру от 1 до 3")
    return pl2_coins



coins = 15
print("coins ", coins)

while coins > 0:

    coins -= pl1_coins()
    print("coins ", coins)
    if coins <= 0:
        print("Победил Игрок2")

    coins -= pl2_coins()
    print("coins ", coins)
    if coins <= 0:
        print("Победил Игрок1")


# Задание-2
# Написать функцию для записи значений словаря в файл
# например
# {
#     "Name":[3,1,2,3,4],
#     "Surname":[3,4,5,6,7,8],
#     "Fathername":[3,4,5,6,7,8]
# }
# т.е. в данном случае создастся три файла name, surname, fathername и внутри на каждой отдельной строке значения из массива
# Name.txt
# 3
# 1
# 2
# 3
# 4
#
# Surname.txt
# 3
# 4
# 5
# 6
# 7
# 8



# Задание***
# Написать класс, который занимается выпечкой тортов.
# т.е. у него есть методы для
# 1) добавления кол-ва ингредиентов на склад
# 2) выпечки с указанием рецепта
# 3) просмотр рецептов
#
# Внутри него зашиты рецепты и в случае если не хватает продуктов, то он говорит каких и сколько ему не хватает
#
