class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def login(self) -> None:
        print(f"Стандартный пользователь {self.name} вошел в базовую систему.")

class Student(User):
    # ПЕРЕОПРЕДЕЛЕНИЕ: Пишем метод с точно таким же именем
    def login(self) -> None:
        print(f"Студент {self.name} авторизовался в портале КБТУ. Загрузка расписания...")

# Проверяем:
basic_user = User("Иван")
student = Student("Алихан")

basic_user.login() # Выведет: Стандартный пользователь Иван вошел в базовую систему.
student.login()    # Выведет: Студент Алихан авторизовался в портале КБТУ...