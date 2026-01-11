from abc import ABC, abstractmethod
import time

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Обработка запроса...")
        time.sleep(2)  # Имитация долгой операции
        return "Результат работы RealSubject"

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject
        self._cache = None
        self._cache_time = 0
        self._cache_ttl = 5  # Время жизни кэша в секундах

    def request(self):
        current_time = time.time()
        
        if (self._cache is not None and 
            current_time - self._cache_time < self._cache_ttl):
            print("Proxy: Возвращаем результат из кэша")
            return self._cache
        
        print("Proxy: Перенаправляем запрос RealSubject")
        result = self._real_subject.request()
        self._cache = result
        self._cache_time = current_time
        return result

if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    
    # Первый запрос - кэшируется
    print("Первый запрос:")
    result = proxy.request()
    print(f"Результат: {result}\n")
    
    # Второй запрос - из кэша
    print("Второй запрос (через 1 секунду):")
    time.sleep(1)
    result = proxy.request()
    print(f"Результат: {result}\n")
    
    # Третий запрос - кэш устарел
    print("Третий запрос (через 6 секунд):")
    time.sleep(6)
    result = proxy.request()
    print(f"Результат: {result}")
