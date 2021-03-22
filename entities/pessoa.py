import MySQLdb

class Pessoa:

    def __init__(self, nome: str, email: str):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f'Nome: {self.nome}, Email: {self.email}'
