class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand  # Public
        self._model = "Unknown"  # Protected
        self.__year = 2024  # Private

    def get_year(self):
      return self.__year


class Car(Vehicle):

    def show_info(self):
        print(f"Brand: {self.brand}")  # ✅ Public доступний
        print(f"Model: {self._model}")  # ✅ Protected доступний
        #print(f"Year: {self.__year}")      # ❌ Private НЕ доступний
        print(f"Year: {self.get_year()}")  # ✅ Через метод батьківського класу


car = Car("Toyota")
car.show_info()