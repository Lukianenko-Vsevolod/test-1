from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        return 'You have created a Windows button.'

class MacButton(Button):
    def paint(self):
        return 'You have created a Mac button.'

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsCheckbox(Checkbox):
    def paint(self):
        return 'You have created a Windows checkbox.'

class MacCheckbox(Checkbox):
    def paint(self):
        return 'You have created a Mac checkbox.'

class GUIFactory(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass
    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass

class WindowsFactory(GUIFactory):
    def createButton(self) -> Button:
        return WindowsButton()
    def createCheckbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()
    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.createButton()
        self.checkbox = factory.createCheckbox()
    def paint(self):
        return self.button.paint(), self.checkbox.paint()
