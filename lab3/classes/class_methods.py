#method its like a def but in into class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Обычный метод класса
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# using methods we can upgrade our code like that
class Player:
    def __init__(self, nickname: str, level: int = 1) -> None:
        self.nickname = nickname
        self.level = level

    # Метод, который использует данные объекта
    def get_status(self) -> str:
        # Используем f-строки (f"...") — это быстрее и чище
        return f"Игрок {self.nickname} (Уровень: {self.level})"

    # Метод, который ИЗМЕНЯЕТ данные объекта
    def level_up(self, levels_earned: int = 1) -> None:
        """Повышает уровень игрока на заданное значение."""
        self.level += levels_earned
        print(f"{self.nickname} повысил уровень! Теперь уровень: {self.level}")

# Создаем объект
gamer = Player("svltanxs")

# Вызываем методы через точку
print(gamer.get_status())  # Выведет: Игрок svltanxs (Уровень: 1)

# Вызываем метод с аргументом
gamer.level_up(4)          # В self передастся объект gamer, в levels_earned передастся 4