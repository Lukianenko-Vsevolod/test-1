"""
Singleton Pattern (Одиночка)
Гарантирует, что у класса есть только один экземпляр
"""

class SingletonMeta(type):
    """
    Метакласс для реализации Singleton
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"🆕 Создаём новый экземпляр {cls.__name__}")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            print(f"♻️ Используем существующий экземпляр {cls.__name__}")
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """
    Пример Singleton: подключение к базе данных
    """
    def __init__(self, connection_string="localhost:5432"):
        self.connection_string = connection_string
        self.is_connected = False
        print(f"🔌 Инициализация БД: {connection_string}")
    
    def connect(self):
        """Установка соединения"""
        if not self.is_connected:
            self.is_connected = True
            return f"✅ Подключено к {self.connection_string}"
        return "⚠️ Уже подключено"
    
    def execute(self, query: str) -> str:
        """Выполнение SQL запроса"""
        return f"📋 Выполняем: {query}"


class ConfigManager(metaclass=SingletonMeta):
    """
    Ещё один пример Singleton: менеджер конфигурации
    """
    def __init__(self):
        self.config = {}
        print("⚙️ Инициализация ConfigManager")
    
    def set(self, key: str, value):
        """Установка значения"""
        self.config[key] = value
        print(f"📝 Установка: {key} = {value}")
    
    def get(self, key: str):
        """Получение значения"""
        return self.config.get(key, None)


def demonstrate_singleton():
    """Демонстрация работы Singleton"""
    print("\n" + "=" * 60)
    print("🎯 ДЕМОНСТРАЦИЯ SINGLETON (Одиночка)")
    print("=" * 60)
    
    print("\n1. Создаём первый экземпляр DatabaseConnection:")
    db1 = DatabaseConnection("postgres://localhost:5432/mydb")
    
    print("\n2. Пытаемся создать второй экземпляр:")
    db2 = DatabaseConnection("mysql://localhost:3306/test")
    
    print("\n3. Проверяем, что это один и тот же объект:")
    print(f"   db1 is db2: {db1 is db2}")
    print(f"   ID db1: {id(db1)}")
    print(f"   ID db2: {id(db2)}")
    print(f"   Параметры db2: {db2.connection_string}")  # Покажет первый connection_string!
    
    print("\n4. Используем ConfigManager:")
    config1 = ConfigManager()
    config1.set("app_name", "MyApp")
    config1.set("version", "1.0.0")
    
    config2 = ConfigManager()  # Получим существующий экземпляр
    print(f"   Получаем настройку из config2: {config2.get('app_name')}")
    print(f"   config1 is config2: {config1 is config2}")
    
    print("\n5. Работа с базой данных:")
    print(f"   {db1.connect()}")
    print(f"   Результат запроса: {db1.execute('SELECT * FROM users')}")
    
    print("\n" + "=" * 60)
    print("✅ SINGLETON: Всегда получаем один и тот же экземпляр!")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_singleton()
