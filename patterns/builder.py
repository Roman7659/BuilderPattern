# Будівельник
class CarBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model

    def set_engine(self, engine):
        self.car.engine = engine

    def set_wheels(self, wheels):
        self.car.wheels = wheels

    def get_result(self):
        return self.car

# Продукт (Об'єкт, що будується)
class Car:
    def __init__(self):
        self.model = None
        self.engine = None
        self.wheels = None

    def __str__(self):
        return f"Car: {self.model}, Engine: {self.engine}, Wheels: {self.wheels}"

# Директор
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_sports_car(self):
        self.builder.reset()
        self.builder.set_model("Sports Car")
        self.builder.set_engine("V8")
        self.builder.set_wheels("20-inch Alloy Wheels")

# Використання патерну Будівельник
builder = CarBuilder()
director = Director(builder)

director.construct_sports_car()
car = builder.get_result()

print(car)  # Результат: Car: Sports Car, Engine: V8, Wheels: 20-inch Alloy Wheels
 
