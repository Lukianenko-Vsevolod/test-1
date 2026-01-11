class EuropeanSocket:
    def voltage(self):
        return 230
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
    def earth(self):
        return 0

class USASocket:
    def voltage(self):
        return 110
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1

class AmericanKettle:
    def __init__(self, power):
        self.power = power
        self.plug = None
    
    def boil(self):
        if self.plug:
            if self.plug.voltage() == 110:
                print(f"Чайник кипятит воду с мощностью {self.power}W")
                return True
            else:
                print("Ошибка: неверное напряжение!")
                return False
        else:
            print("Чайник не подключен к розетке")
            return False

class SocketAdapter:
    def __init__(self, european_socket):
        self._european_socket = european_socket
    
    def voltage(self):
        # Преобразуем 230V в 110V
        return 110
    
    def live(self):
        return self._european_socket.live()
    
    def neutral(self):
        return self._european_socket.neutral()
    
    def earth(self):
        return self._european_socket.earth()

if __name__ == "__main__":
    # Европейская розетка
    european_socket = EuropeanSocket()
    print(f"Европейская розетка: {european_socket.voltage()}V")
    
    # Американский чайник
    kettle = AmericanKettle(1500)
    
    # Попытка подключить напрямую (не сработает)
    kettle.plug = european_socket
    print("\nПопытка подключить к европейской розетке напрямую:")
    kettle.boil()
    
    # Используем адаптер
    adapter = SocketAdapter(european_socket)
    kettle.plug = adapter
    print("\nИспользование адаптера:")
    kettle.boil()
