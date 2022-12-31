
class Input:
    # Класс для обработки и иницилизации данных.
    def __init__(self):
        inputList = []
        for quest in ["Введите название csv-файла: ", "Введите название профессии: "]:
            print(quest, end="")
            inputList.append(input())
        self.filteCsv = inputList[0]
        self.profession = inputList[1]
