
class Input:
    """
    Класс для обработки и иницилизации данных
    """

    def __init__(self):
        input_data = []
        for question in ["Введите название csv-файла: ", "Введите название профессии: "]:
            print(question, end="")
            input_data.append(input())
        self.csv_file = input_data[0]
        self.profession = input_data[1]
