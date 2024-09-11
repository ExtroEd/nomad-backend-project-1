"""
Домашнее задание №1.
Дата: 10.09.2024.
Название: ООП (наследование).
"""

class Transport:
    def __init__(self, brand, model, year):
        # Инициализация основных атрибутов транспортного средства
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def start(self):
        # Увеличение скорости на 10 км/ч
        self.speed += 10
        return f"Скорость увеличена до {self.speed} км/ч"

    def stop(self):
        # Сброс скорости до 0 км/ч
        self.speed = 0
        return f"Скорость сброшена до {self.speed} км/ч"

    def get_info(self):
        # Вывод общей информации о транспортном средстве
        return (
            f"Марка: {self.brand}, Модель: {self.model}, "
            f"Год выпуска: {self.year}, Скорость: {self.speed} км/ч"
        )


class Car(Transport):
    def __init__(self, brand, model, year, engine_type):
        super().__init__(brand, model, year)
        self.engine_type = engine_type

    def get_info(self):
        # Добавление информации о типе двигателя к общей информации
        info = super().get_info()
        return f"{info}, Тип двигателя: {self.engine_type}"


class Bicycle(Transport):
    def __init__(self, brand, model, year, bicycle_type):
        super().__init__(brand, model, year)
        self.bicycle_type = bicycle_type

    def get_info(self):
        # Добавление информации о типе велосипеда к общей информации
        info = super().get_info()
        return f"{info}, Тип велосипеда: {self.bicycle_type}"


class Train(Transport):
    def __init__(self, brand, model, year, carriages):
        super().__init__(brand, model, year)
        self.carriages = carriages

    def get_info(self):
        # Добавление информации о количестве вагонов к общей информации
        info = super().get_info()
        return f"{info}, Количество вагонов: {self.carriages}"

# Создание объектов различных транспортных средств
car = Car("Rolls Royce", "Phantom", 2024, "бензиновый")
bike = Bicycle("Giant", "Trance X Advanced Pro", 2022, "горный")
train = Train("Votkinsk plant", "Barguzin", 2017, 12)

# Вывод информации о каждом транспортном средстве с форматированием

print("=" * 30)
print("Информация об автомобиле:")
print(car.get_info())
print("-" * 30)

print("Информация о велосипеде:")
print(bike.get_info())
print("-" * 30)

print("Информация о поезде:")
print(train.get_info())
print("=" * 30)

# Изменение скорости с поясняющими заголовками
print("\nНачало движения...")
print("=" * 30)

print("Увеличение скорости автомобиля:")
print(car.start())
print(car.get_info())
print("-" * 30)

print("Увеличение скорости велосипеда:")
print(bike.start())
print(bike.get_info())
print("-" * 30)

print("Увеличение скорости поезда:")
print(train.start())
print(train.get_info())
print("=" * 30)

# Остановка транспортных средств
print("\nОстановка транспортных средств...")
print("=" * 30)

print("Остановка автомобиля:")
print(car.stop())
print(car.get_info())
print("-" * 30)

print("Остановка велосипеда:")
print(bike.stop())
print(bike.get_info())
print("-" * 30)

print("Остановка поезда:")
print(train.stop())
print(train.get_info())
print("=" * 30)
