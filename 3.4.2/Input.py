
class Input:

    # Класс для обработки и иницилизации данных

    def __init__(self):
        inputs = []
        for quest in ["Введите название csv-файла: ", "Введите название профессии: "]:
            print(quest, end="")
            inputs.append(input())
        self.fileCsv = inputs[0]
        self.profession = inputs[1]
