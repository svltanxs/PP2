import json

# --- 1. Parsing JSON: json.loads() (Строка -> Python) ---
# Представим, мы получили этот ответ от API
json_string = '{"name": "Dias", "age": 19, "is_student": true, "items": null}'

python_dict = json.loads(json_string)
print(type(python_dict))       # Вывод: <class 'dict'>
print(python_dict["name"])     # Вывод: Dias
print(python_dict["is_student"]) # Вывод: True (с большой буквы, т.к. это уже Python)

# --- 2. Converting Python to JSON: json.dumps() (Python -> Строка) ---
my_data = {
    "user": "Almaty_Gamer",
    "score": 1500,
    "inventory": ["sword", "shield"]
}

# indent=4 делает красивый формат с отступами (pretty print)
json_output = json.dumps(my_data, indent=4)
print(json_output)
# Вывод:
# {
#     "user": "Almaty_Gamer",
#     "score": 1500,
#     "inventory": [
#         "sword",
#         "shield"
#     ]
# }