my_list = ["яблоко", "банан", "вишня"]

# Получаем Итератор (Iterator) с помощью функции iter()
my_iter = iter(my_list)

# Запрашиваем элементы по одному с помощью next()
print(next(my_iter))  # Вывод: яблоко
print(next(my_iter))  # Вывод: банан
print(next(my_iter))  # Вывод: вишня
#---------------------------------------------------
my_tuple = (10, 20, 30)

# Под капотом цикл for создает итератор из my_tuple
# и вызывает next() на каждой итерации.
for x in my_tuple:
    print(x)
#---------------------------------------------------
class CountUpTo:
    def __init__(self, limit):
        self.limit = limit

    # Инициализирует состояние и возвращает сам объект
    def __iter__(self):
        self.current = 1
        return self

    # Содержит логику выдачи следующего элемента
    def __next__(self):
        if self.current <= self.limit:
            x = self.current
            self.current += 1  # Обновляем состояние для следующего вызова
            return x
        else:
            # Если достигли лимита, сигнализируем об остановке
            raise StopIteration

# Использование нашего кастомного итератора
counter = CountUpTo(3)
for num in counter:
    print(num) 
# Вывод:
# 1
# 2
# 3
#---------------------------------------------------
def count_up_to_gen(limit):
    current = 1
    # Пока текущее значение меньше или равно лимиту
    while current <= limit:
        yield current      # Отдаем значение и СТАВИМ НА ПАУЗУ
        current += 1       # При следующем вызове next() код продолжится отсюда

# При вызове функции-генератора ее код не выполняется сразу!
# Вместо этого она возвращает объект-генератор.
gen_obj = count_up_to_gen(3)

print(next(gen_obj)) # Вывод: 1. Функция дошла до yield и уснула.
print(next(gen_obj)) # Вывод: 2. Функция проснулась, current стал 2, цикл повторился.
print(next(gen_obj)) # Вывод: 3.
#---------------------------------------------------
import sys

# Генератор списка (List Comprehension): 
# Вычисляет ВСЕ 100,000 квадратов чисел сразу и сохраняет их в память.
squares_list = [x**2 for x in range(100000)]
print(f"Размер списка в памяти: {sys.getsizeof(squares_list)} байт") 
# Выведет около 800,000 байт

# Выражение-генератор (Generator Expression):
# Не вычисляет ничего заранее. Создает только объект-"рецепт", 
# который будет выдавать по одному числу за раз.
squares_gen = (x**2 for x in range(100000))
print(f"Размер генератора в памяти: {sys.getsizeof(squares_gen)} байт") 
# Выведет около 100-200 байт (в тысячи раз меньше!)

# Получаем первые два значения из генератора
print(next(squares_gen)) # Вывод: 0 (0**2)
print(next(squares_gen)) # Вывод: 1 (1**2)
