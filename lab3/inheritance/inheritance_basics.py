# this is a regular class 
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def login(self) -> None:
        print(f"Пользователь {self.name} вошел в систему.")
# this is child class

class Student(User):
    pass

# Теперь мы можем создать студента, и он АВТОМАТИЧЕСКИ умеет всё то же, что и User
student1 = Student("Алихан", "ali@example.com")
student1.login() # Выведет: Пользователь Алихан вошел в систему.
# but we cant do __init__ here because parents init dominated childs so we use super()