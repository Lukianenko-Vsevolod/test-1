"""
Builder Pattern (Строитель)
Поэтапное создание сложных объектов
"""

from abc import ABC, abstractmethod
from typing import List


class Pizza:
    """
    Продукт: Пицца
    """
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings: List[str] = []
        self.cheese = ""
        self.size = ""
        self.spice_level = ""
    
    def __str__(self) -> str:
        return (
            f"\n🍕 ПИЦЦА: {self.name}\n"
            f"{'='*30}\n"
            f"  Размер:      {self.size}\n"
            f"  Тесто:       {self.dough}\n"
            f"  Соус:        {self.sauce}\n"
            f"  Сыр:         {self.cheese}\n"
            f"  Острота:     {self.spice_level}\n"
            f"  Начинка:     {', '.join(self.toppings) if self.toppings else 'нет'}\n"
            f"{'='*30}"
        )


class PizzaBuilder(ABC):
    """
    Абстрактный строитель
    """
    def __init__(self):
        self.pizza = Pizza()
    
    @abstractmethod
    def set_name(self):
        pass
    
    @abstractmethod
    def prepare_dough(self):
        pass
    
    @abstractmethod
    def add_sauce(self):
        pass
    
    @abstractmethod
    def add_cheese(self):
        pass
    
    @abstractmethod
    def add_toppings(self):
        pass
    
    @abstractmethod
    def set_size(self):
        pass
    
    @abstractmethod
    def set_spice_level(self):
        pass
    
    def get_pizza(self) -> Pizza:
        return self.pizza


class MargheritaBuilder(PizzaBuilder):
    """
    Строитель для пиццы Маргарита
    """
    def set_name(self):
        self.pizza.name = "Маргарита"
        print("  🏷️  Название: Маргарита")
    
    def prepare_dough(self):
        self.pizza.dough = "Тонкое итальянское тесто"
        print("  🍞 Тесто: Тонкое итальянское")
    
    def add_sauce(self):
        self.pizza.sauce = "Томатный соус"
        print("  🍅 Соус: Томатный")
    
    def add_cheese(self):
        self.pizza.cheese = "Моцарелла"
        print("  🧀 Сыр: Моцарелла")
    
    def add_toppings(self):
        self.pizza.toppings = ["Свежие помидоры", "Базилик"]
        print("  🍅 Начинка: Помидоры, Базилик")
    
    def set_size(self):
        self.pizza.size = "Средняя (30 см)"
        print("  📏 Размер: Средняя (30 см)")
    
    def set_spice_level(self):
        self.pizza.spice_level = "Не острая"
        print("  🌶️  Острота: Не острая")


class PepperoniBuilder(PizzaBuilder):
    """
    Строитель для пиццы Пепперони
    """
    def set_name(self):
        self.pizza.name = "Пепперони"
        print("  🏷️  Название: Пепперони")
    
    def prepare_dough(self):
        self.pizza.dough = "Традиционное дрожжевое тесто"
        print("  🍞 Тесто: Традиционное дрожжевое")
    
    def add_sauce(self):
        self.pizza.sauce = "Острый томатный соус"
        print("  🍅 Соус: Острый томатный")
    
    def add_cheese(self):
        self.pizza.cheese = "Смесь моцареллы и чеддера"
        print("  🧀 Сыр: Моцарелла + Чеддер")
    
    def add_toppings(self):
        self.pizza.toppings = ["Пепперони", "Перец", "Лук", "Грибы"]
        print("  🍕 Начинка: Пепперони, Перец, Лук, Грибы")
    
    def set_size(self):
        self.pizza.size = "Большая (40 см)"
        print("  📏 Размер: Большая (40 см)")
    
    def set_spice_level(self):
        self.pizza.spice_level = "Средняя острота"
        print("  🌶️  Острота: Средняя")


class HawaiianBuilder(PizzaBuilder):
    """
    Строитель для Гавайской пиццы
    """
    def set_name(self):
        self.pizza.name = "Гавайская"
        print("  🏷️  Название: Гавайская")
    
    def prepare_dough(self):
        self.pizza.dough = "Пышное тесто"
        print("  🍞 Тесто: Пышное")
    
    def add_sauce(self):
        self.pizza.sauce = "Сладкий томатный соус"
        print("  🍅 Соус: Сладкий томатный")
    
    def add_cheese(self):
        self.pizza.cheese = "Моцарелла"
        print("  🧀 Сыр: Моцарелла")
    
    def add_toppings(self):
        self.pizza.toppings = ["Ветчина", "Ананас", "Кукуруза"]
        print("  🍍 Начинка: Ветчина, Ананас, Кукуруза")
    
    def set_size(self):
        self.pizza.size = "Средняя (30 см)"
        print("  📏 Размер: Средняя (30 см)")
    
    def set_spice_level(self):
        self.pizza.spice_level = "Не острая"
        print("  🌶️  Острота: Не острая")


class PizzaDirector:
    """
    Директор - управляет процессом сборки
    """
    def __init__(self):
        self.builder = None
    
    def set_builder(self, builder: PizzaBuilder):
        self.builder = builder
    
    def make_pizza(self, with_extra_cheese=False):
        """
        Шаблонный метод сборки пиццы
        """
        print("\n👨‍🍳 Начинаем готовить пиццу...")
        
        # Строгий порядок приготовления
        self.builder.set_name()
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_cheese()
        
        if with_extra_cheese:
            print("  🧀 Добавляем дополнительный сыр!")
            self.builder.pizza.cheese += " (двойная порция)"
        
        self.builder.add_toppings()
        self.builder.set_size()
        self.builder.set_spice_level()
        
        print("  ✅ Пицца готова!")
    
    def get_pizza(self) -> Pizza:
        return self.builder.get_pizza()


def demonstrate_builder():
    """Демонстрация работы Builder"""
    print("\n" + "=" * 60)
    print("🎯 ДЕМОНСТРАЦИЯ BUILDER (Строитель)")
    print("=" * 60)
    
    director = PizzaDirector()
    
    print("\n1. 🍕 ПРИГОТОВЛЕНИЕ МАРГАРИТЫ:")
    print("-" * 40)
    margherita_builder = MargheritaBuilder()
    director.set_builder(margherita_builder)
    director.make_pizza(with_extra_cheese=True)
    margherita = director.get_pizza()
    print(margherita)
    
    print("\n2. 🍕 ПРИГОТОВЛЕНИЕ ПЕППЕРОНИ:")
    print("-" * 40)
    pepperoni_builder = PepperoniBuilder()
    director.set_builder(pepperoni_builder)
    director.make_pizza()
    pepperoni = director.get_pizza()
    print(pepperoni)
    
    print("\n3. 🍕 ПРИГОТОВЛЕНИЕ ГАВАЙСКОЙ:")
    print("-" * 40)
    hawaiian_builder = HawaiianBuilder()
    director.set_builder(hawaiian_builder)
    director.make_pizza()
    hawaiian = director.get_pizza()
    print(hawaiian)
    
    print("\n" + "=" * 60)
    print("✅ BUILDER: Поэтапное создание сложных объектов!")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_builder()
