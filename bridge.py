from abc import ABC, abstractmethod

# Реализация (Implementation)
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass
    
    @abstractmethod
    def enable(self):
        pass
    
    @abstractmethod
    def disable(self):
        pass
    
    @abstractmethod
    def get_volume(self) -> int:
        pass
    
    @abstractmethod
    def set_volume(self, percent: int):
        pass

class TV(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 50
    
    def is_enabled(self) -> bool:
        return self._enabled
    
    def enable(self):
        self._enabled = True
        print("TV включен")
    
    def disable(self):
        self._enabled = False
        print("TV выключен")
    
    def get_volume(self) -> int:
        return self._volume
    
    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self._volume = percent
            print(f"Громкость TV установлена на {percent}%")
        else:
            print("Некорректное значение громкости")

class Radio(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 30
    
    def is_enabled(self) -> bool:
        return self._enabled
    
    def enable(self):
        self._enabled = True
        print("Radio включен")
    
    def disable(self):
        self._enabled = False
        print("Radio выключен")
    
    def get_volume(self) -> int:
        return self._volume
    
    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self._volume = percent
            print(f"Громкость Radio установлена на {percent}%")
        else:
            print("Некорректное значение громкости")

# Абстракция (Abstraction)
class RemoteControl:
    def __init__(self, device: Device):
        self._device = device
    
    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()
    
    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)
    
    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.set_volume(0)
        print("Режим без звука")

if __name__ == "__main__":
    tv = TV()
    radio = Radio()
    
    print("Работа с TV:")
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.volume_up()
    remote.volume_down()
    
    print("\nРабота с Radio:")
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.volume_up()
    advanced_remote.mute()
