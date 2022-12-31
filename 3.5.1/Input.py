
class Input:
    # Класс для обработки и иницилизации данных.
    def __init__(self):
        inputArray = []
        for quest in ["Введите название csv-файла: ", "Введите название профессии: "]:
            print(quest, end="")
            inputArray.append(input())
        self.fileCsv = inputArray[0]
        self.profession = inputArray[1]
