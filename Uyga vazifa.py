
#  1 chi masala:

# class Country:
#     def __init__(self, name, area, population, borders: list):
#         self.__name = name
#         self.__area = area
#         self.__population = population
#         self.__borders = borders
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, naw_name):
#         self.__name == naw_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
#
#     @property
#     def area(self):
#         return self.__name
#
#     @area.setter
#     def area(self, new_area):
#         self.__area == new_area
#
#     @area.deleter
#     def area(self):
#         del self.__area
#
#
#
#     @property
#     def populaton(self):
#         return self.__population
#
#     @populaton.setter
#     def population(self, new_population):
#         self.__population == new_population
#
#     @populaton.deleter
#     def population(self):
#         del self.__population
#
#
#
#     @property
#     def borders(self):
#         return self.__borders
#
#     @borders.setter
#     def borders(self, new_borders):
#         self.__borders == new_borders
#
#     @borders.deleter
#     def borders(self):
#         del self.__borders
#
#     def country_info(self):
#         return f"Nomi: - {self.__name} Maydoni: -  {self.__area} Aholisi: -  {self.__population} Qushnilari: -  {self.__borders}"
#
#
#
# user1 = Country("Uzbekistan", "448.8", 36000000, "Qazogiston, Qirg'iziston, Tojikiston, Turkmaniston, Afg'oniston")
# # print(user1.country_info())
# user1.name = "Italiya"
# user1.area = "301.230"
# user1.populaton = "58103033"
# user1.borders = "Apenin, Sitsiliya, Sadrina, Elba, Monte_Roza"
# print("==============================================================================================================================")
# print(user1.name)
# print(user1.area)
# print(user1.populaton)
# print(user1.populaton)
# print(user1.borders)

#============================================================================================================================================

# 2 chi masala
# from abc import ABC,abstractmethod
#
# class OS(ABC):
#     def __init__(self, name, version, year_issue):
#         self.name = name
#         self.version = version
#         self.year_issue = year_issue
#
#
#     def get_name(self):
#         pass
#
#
#     @abstractmethod
#     def get_version(self):
#         pass
#
#
#     @abstractmethod
#     def get_year_issue(self):
#         pass
#
#
#
# class Linux(OS):
#     def __init__(self, name, version, year_issue):
#         super().__init__(name, version, year_issue)
#
#     def get_name(self):
#         return f"Operatsion siystem name {self.name}"
#
#     def get_version(self):
#         return f"This varsion {self.version}"
#
#     def get_year_issue(self):
#         return f"This year  {self.year_issue}"
#
#
# class Max(OS):
#     def __init__(self, name, version, year_issue):
#         super().__init__(name, version, year_issue)
#
#     def get_name(self):
#         return f"Operatsion siystem name {self.name}"
#
#     def get_version(self):
#         return f"This varsion {self.version}"
#
#     def get_year_issue(self):
#         return f"This year  {self.year_issue}"
#
#
# class Win(OS):
#     def __init__(self, name, version, year_issue):
#         super().__init__(name, version, year_issue)
#
#     def get_name(self):
#         return f"Operatsion siystem name {self.name}"
#
#     def get_version(self):
#         return f"This varsion {self.version}"
#
#     def get_year_issue(self):
#         return f"This year  {self.year_issue}"
#
#
#
#
#
#
# user2 = Linux("Linux", 12, 2023)
# print(user2.name)
# print(user2.version)
# print(user2.year_issue)
#
# print("==================================================")
#
#
# user3 = Max("Max", 10, 2019)
# print(user3.name)
# print(user3.version)
# print(user3.year_issue)
#
# print("==================================================")
#
# user4 = Win("Win", 11, 2022)
# print(user4.name)
# print(user4.version)
# print(user4.year_issue)




























