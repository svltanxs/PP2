# super its like a init in childs class
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def login(self) -> None:
        print(f"[{self.email}] {self.name} в сети.")

# Наследуемся от User
class Student(User):
    # Добавляем новый аргумент github_repo
    def __init__(self, name: str, email: str, github_repo: str) -> None:
        
        # 1. Сначала отдаем name и email родителю (User), чтобы он сам их сохранил
        super().__init__(name, email)
        # User.__init__(name,email) so we can write like that
        # 2. Теперь сохраняем то, что относится ТОЛЬКО к студенту
        self.github_repo = github_repo

    # 3. Добавляем метод, который есть только у студента
    def push_lab(self, subject: str) -> None:
        print(f"Студент {self.name} загрузил код по предмету '{subject}' в репозиторий {self.github_repo}")

# --- Проверяем в деле ---
my_student = Student("Ернар", "ernar@test.kz", "svltanxs/PP2")

my_student.login() # Работает родительский метод
my_student.push_lab("Programming Principles II") # Работает собственный метод