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



coins = 25
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


def write_file_dic(dic: dict):
    for key in dict.keys(dic):
        with open(f'{key}.txt', 'w', encoding='utf-8') as f:
            for i in dic[key]:
                f.write(f"{i}" + '\n')


write_file_dic({
    "Name":[3,1,2,3,4],
    "Surname":[3,4,5,6,7,8],
    "Fathername":[3,4,5,6,7,8]
})

# Задание***
# Написать класс, который занимается выпечкой тортов.
# т.е. у него есть методы для
# 1) добавления кол-ва ингредиентов на склад
# 2) выпечки с указанием рецепта
# 3) просмотр рецептов
#
# Внутри него зашиты рецепты и в случае если не хватает продуктов, то он говорит каких и сколько ему не хватает
#


#***** Добавлено от преподователя *****

class BakeryMaker:
    def __init__(self):
        # {
        #     "recipe_name": {
        #         "ing1": 10,
        #         "ing2": 10,
        #         "ing3": 10,
        #     }
        # }
        self.recipes = dict()

        # {
        #   "ing1": 10,
        #   "ing2": 10,
        #   "ing3": 10,
        # }
        self.ingredients = dict()

    def add_ingredients(self, ingredients: dict) -> None:
        for k, v in ingredients.items():
            if k in self.ingredients:
                self.ingredients[k] += v
            else:
                self.ingredients[k] = v

    def push_recipes(self, recipes: dict):
        for k, v in recipes.items():
            self.recipes[k] = v

    def print_ingredients(self):
        print("В холодильнике имеется: ")
        for ing_name, ing_value in self.ingredients.items():
            print(f"{ing_name}:{ing_value}")

    def print_recipes(self):
        for recipe_name, recipe_dict in self.recipes.items():
            print(f"{recipe_name}")
            for ing_name, ing_value in recipe_dict.items():
                print(f"\t{ing_name}:{ing_value}")

    def get_buy_list(self, recipe_name):
        res = dict()
        for name, value in self.recipes[recipe_name].items():
            if name not in self.ingredients:
                res[name] = value
            elif self.ingredients[name] < value:
                res[name] = value - self.ingredients[name]
        return res

    def subtract_ingredients(self, recipe_name):
        for name, value in self.recipes[recipe_name].items():
            self.ingredients[name] -= value

    def make_cake(self, recipe_name):
        print(f"Пробуем делать {recipe_name}")
        if recipe_name in self.recipes:
            buy_list = self.get_buy_list(recipe_name)
            if len(buy_list) == 0:
                print("Продуктов хватило делаем")
                self.subtract_ingredients(recipe_name)
                print("Готово")
            else:
                print("Продуктов не хватило. Докупите: ")
                self.print_buy_list(buy_list)
        else:
            raise Exception("Recipe not found")

    def print_buy_list(self, buy_list):
        for name, value in buy_list.items():
            print(f"{name}: {value}")


cook = BakeryMaker()
recipes = {
    "Блины": {
        "Молоко": 500,
        "Мука": 500,
        "Яйца": 10,
    },
    "Торт": {
        "Мука": 500,
        "Яйца": 10,
        "Сметана": 200
    }
}

not_enough_ingredients = {
    "Молоко": 300,
    "Мука": 300,
    "Яйца": 7
}

enough_ingredients = {
    "Молоко": 300000,
    "Мука": 300000,
    "Яйца": 70000
}

cook.push_recipes(recipes)
cook.add_ingredients(not_enough_ingredients)
cook.print_recipes()
cook.print_ingredients()
cook.make_cake("Блины")
cook.add_ingredients(enough_ingredients)
cook.print_ingredients()
cook.make_cake("Блины")
cook.print_ingredients()
