Поиск вакансий на hh.ru

Проект использует следующие технологии:
- requests
- python 3.11
- pytest

Что происходит в приложении:
- с платформы hh.ru выгружается в json-файл список вакансий по заданному пользователем ключевому слову
- в случае ошибки, при вводе ключевого слова, файл можно удалить и начать работу сначала
- из сформированного списка вакансий формируется новый список, в который выгружаются только пять атрибутов вакансий 
(название, город, зарплата, ссылка на сайТ, требования к вакансии)
- взаимодействие пользователя происходит через консоль
- по запросу пользователя формируются: список вакансий по ключевому слову, отсортированный по зарплате список вакансий, выборку из сформированного списка по ключевому слову


Техническое задание:

Написать программу, которая будет получать информацию о вакансиях с платформы hh.ru в России, сохранять ее в файл и позволять удобно работать с ней: добавлять, фильтровать, удалять.

Требования к реализации:

- Создать абстрактный класс для работы с API сервиса с вакансиями. 
- Реализовать класс, наследующийся от абстрактного класса, для работы с платформой hh.ru. Класс должен уметь подключаться к API и получать вакансии.
- Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п. (всего не менее четырех атрибутов). 
- Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
Способами валидации данных может быть проверка, указана или нет зарплата. В этом случае выставлять значение зарплаты 0 или «Зарплата не указана» в зависимости от структуры класса.
- Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях. 
- Создать класс для сохранения информации о вакансиях в JSON-файл. Данный класс выступит в роли основы для коннектора, заменяя который (класс-коннектор), можно использовать в качестве хранилища одну из баз данных или удаленное хранилище со своей специфической системой обращений.
- Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем через консоль. 
- Возможности этой функции должны быть следующими:
ввести поисковый запрос для запроса вакансий из hh.ru;
получить топ N вакансий по зарплате (N запрашивать у пользователя);
получить вакансии с ключевым словом в описании.

Объединить все классы и функции в единую программу.
Покрыть описанный функционал тестами.


Требования к реализации в парадигме ООП:
- Абстрактный класс и классы для работы с API платформ с вакансиями должны быть реализованы в соответствии с принципом наследования.
- Класс для работы с вакансиями должен быть реализован в соответствии с принципом инкапсуляции и поддерживать методы сравнения вакансий между собой по зарплате.
- Классы и другие сущности в проекте должны удовлетворять минимум первым двум требованиям принципов SOLID.


Выходные данные:
- Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
- Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.
