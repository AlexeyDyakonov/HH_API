import sys
from src.json import WorkWithJson
from src.api import HH
from src.vacancy import Vacancy


class UserInteractive(WorkWithJson):
    """
    Класс, обеспечивающий взаимодействие с пользователем
    """

    def __init__(self, user_name: str):
        super().__init__()
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword: str):
        """
        Получение с сайта HH списка вакансий
        """

        hh = HH(keyword)
        return hh.load_vacancies()

    def get_vacancies_list_from_file(self) -> list[dict]:
        """
        Получение из файла списка вакансий
        """

        work_file = WorkWithJson()
        self.vacancies_list = []
        for vac in work_file.read_file():
            self.vacancies_list.append(vac)
        return self.vacancies_list

    def get_top_n_for_salary(self, n: int) -> list[dict]:
        """
        Получение заданного пользователем количества вакансий с сортировкой
        по уровню зарплат (с убыванием)
        """

        vac_filter = []
        for vac in self.vacancies_list:
            vac_filter.append(vac)

        sort_by_salary = sorted(vac_filter, key=lambda x: x.salary, reverse=True)
        return sort_by_salary[:n]

    def get_vacancy_from_keywords(self) -> list[dict]:
        """
        Получение списка вакансий по заданному ключевому слову

        """
        keywords = input("Введите ключевое слово:  ")
        print()
        res = []
        for vacancy in self.vacancies_list:
            if vacancy.name.find(keywords) != -1:
                res.append(vacancy)

        return res

    @staticmethod
    def user_interaction(self):
        """
        Функция для взаимодействия с пользователем
        """
        user_name = input("Привет, как тебя зовут?  ")
        user = UserInteractive(user_name)

        keyword = input(f"{user_name} какая вакансия тебя интересует? ")

        user.save_file(user.get_vacancies_list(keyword))

        YesNo = input(f"{user_name} файл с вакансиями сформирован.\n"
                      "Удалить файл с найденными вакансиями?\n"
                      "Если удаляем, то выходим из программы!\n"
                      "(Д/д, Y/y - удаляем и выходим, Н/н, N/n - продолжаем работу): ")
        if YesNo == "Y" or YesNo == "y" or YesNo == "Д" or YesNo == "д":
            user.delete_file()
            sys.exit()

        n = int(input("Сколько вакансий вывести на экран, введите число: "))
        print()

        user.get_vacancies_list_from_file()
        new_vac_list = []
        for vacancy in user.vacancies_list:
            vac = Vacancy.new_vacancy(vacancy)
            new_vac_list.append(vac)

        user.vacancies_list = new_vac_list
        user.get_top_n_for_salary(n)
        for vacancy in user.get_top_n_for_salary(n):
            print(vacancy)

        print("------------------------------------------------------------------")
        for vacancy in user.get_vacancy_from_keywords():
            print(vacancy)