class Student:
    # Этот метод сработает автоматически при создании студента
    def __init__(self, name, age):
        self.name = name  # Сохраняем переданное имя внутрь объекта
        self.age = age    # Сохраняем возраст

# Создаем объекты. Данные в скобках автоматически летят в __init__
student1 = Student("Алихан", 18)
student2 = Student("Томирис", 19)

print(f"Студент {student1.name}, возраст: {student1.age}")
