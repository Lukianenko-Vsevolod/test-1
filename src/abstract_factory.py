"""
Abstract Factory Pattern (Абстрактная фабрика)
Создание семейств связанных объектов
"""

from abc import ABC, abstractmethod
from enum import Enum


class Theme(Enum):
    """Темы оформления"""
    LIGHT = "light"
    DARK = "dark"
    RETRO = "retro"


# Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def click(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def toggle(self) -> str:
        pass


class TextField(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def input(self, text: str) -> str:
        pass


# Light Theme продукты
class LightButton(Button):
    def render(self) -> str:
        return "🔘 [Light Button] Белая кнопка с синей рамкой"
    
    def click(self) -> str:
        return "🖱️ Light button clicked: Мягкий клик"


class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "☐ [Light Checkbox] Светлый квадратик"
    
    def toggle(self) -> str:
        return "🔘 Light checkbox toggled: Плавная анимация"


class LightTextField(TextField):
    def render(self) -> str:
        return "📝 [Light Text Field] Белое поле с серой рамкой"
    
    def input(self, text: str) -> str:
        return f"✍️ Light input: '{text}' (чёрный текст)"


# Dark Theme продукты
class DarkButton(Button):
    def render(self) -> str:
        return "🔳 [Dark Button] Тёмная кнопка с фиолетовым свечением"
    
    def click(self) -> str:
        return "🖱️ Dark button clicked: Глубокий звук"


class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "⬜ [Dark Checkbox] Тёмный квадрат"
    
    def toggle(self) -> str:
        return "🔘 Dark checkbox toggled: Эффект вспышки"


class DarkTextField(TextField):
    def render(self) -> str:
        return "📝 [Dark Text Field] Чёрное поле с синей подсветкой"
    
    def input(self, text: str) -> str:
        return f"✍️ Dark input: '{text}' (белый текст)"


# Retro Theme продукты
class RetroButton(Button):
    def render(self) -> str:
        return "🎮 [Retro Button] Пиксельная кнопка 8-bit"
    
    def click(self) -> str:
        return "🖱️ Retro button clicked: Звук из 80-х!"


class RetroCheckbox(Checkbox):
    def render(self) -> str:
        return "🧱 [Retro Checkbox] Блочный пиксельный чекбокс"
    
    def toggle(self) -> str:
        return "🔘 Retro checkbox toggled: Пиксельная анимация"


class RetroTextField(TextField):
    def render(self) -> str:
        return "📟 [Retro Text Field] Зелёный терминальный вид"
    
    def input(self, text: str) -> str:
        return f"⌨️ Retro input: '{text}' (зелёный моноширинный шрифт)"


# Абстрактная фабрика
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
    
    @abstractmethod
    def create_text_field(self) -> TextField:
        pass


# Конкретные фабрики
class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()
    
    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()
    
    def create_text_field(self) -> TextField:
        return LightTextField()


class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()
    
    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()
    
    def create_text_field(self) -> TextField:
        return DarkTextField()


class RetroThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return RetroButton()
    
    def create_checkbox(self) -> Checkbox:
        return RetroCheckbox()
    
    def create_text_field(self) -> TextField:
        return RetroTextField()


# Клиентское приложение
class Application:
    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None
        self.text_field = None
    
    def create_ui(self):
        """Создание интерфейса"""
        print("🛠️ Создаём UI компоненты...")
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
        self.text_field = self.factory.create_text_field()
    
    def render(self):
        """Отрисовка интерфейса"""
        print("\n🎨 Отрисованный интерфейс:")
        print(f"  • {self.button.render()}")
        print(f"  • {self.checkbox.render()}")
        print(f"  • {self.text_field.render()}")
    
    def interact(self):
        """Взаимодействие с интерфейсом"""
        print("\n👆 Взаимодействие:")
        print(f"  • {self.button.click()}")
        print(f"  • {self.checkbox.toggle()}")
        print(f"  • {self.text_field.input('Hello World!')}")


# Фабрика фабрик
class ThemeFactory:
    @staticmethod
    def get_factory(theme: Theme) -> UIFactory:
        factories = {
            Theme.LIGHT: LightThemeFactory(),
            Theme.DARK: DarkThemeFactory(),
            Theme.RETRO: RetroThemeFactory()
        }
        return factories[theme]


def demonstrate_abstract_factory():
    """Демонстрация работы Abstract Factory"""
    print("\n" + "=" * 60)
    print("🎯 ДЕМОНСТРАЦИЯ ABSTRACT FACTORY (Абстрактная фабрика)")
    print("=" * 60)
    
    themes = [Theme.LIGHT, Theme.DARK, Theme.RETRO]
    
    for theme in themes:
        print(f"\n{'='*40}")
        print(f"🎨 ТЕМА: {theme.value.upper()}")
        print('='*40)
        
        factory = ThemeFactory.get_factory(theme)
        app = Application(factory)
        app.create_ui()
        app.render()
        app.interact()
    
    print("\n" + "=" * 60)
    print("✅ ABSTRACT FACTORY: Создаём согласованные семейства объектов!")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_abstract_factory()
