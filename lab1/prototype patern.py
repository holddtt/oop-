class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def clone(self):
        # Використовуємо прототип для створення нового об'єкта
        return Car(self.brand, self.model, self.color)

# Створюємо оригінальний об'єкт
original_car = Car("Toyota", "Camry", "Blue")

# Клонуємо його за допомогою прототипу
cloned_car = original_car.clone()

# Результат: маємо два об'єкти з однаковими властивостями
print(original_car.brand, original_car.model, original_car.color)  # Toyota Camry Blue
print(cloned_car.brand, cloned_car.model, cloned_car.color)       # Toyota Camry Blue
