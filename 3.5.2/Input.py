
class Input:

    # Класс для обработки и иницилизации данных.
    def __init__(self):
        inputUser = []
        for quest in ["Введите название csv-файла: ", "Введите название профессии: "]:
            print(quest, end="")
            inputUser.append(input())
        self.csv = inputUser[0]
        self.profession = inputUser[1]
