from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return f"Handler A обработал запрос {request}"
        else:
            print("Handler A передает дальше")
            return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return f"Handler B обработал запрос {request}"
        else:
            print("Handler B передает дальше")
            return super().handle(request)

class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request == "C":
            return f"Handler C обработал запрос {request}"
        else:
            print("Handler C не может обработать")
            return super().handle(request)

if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()

    handler_a.set_next(handler_b).set_next(handler_c)

    requests = ["A", "B", "C", "D"]
    for request in requests:
        print(f"\nОбработка запроса: {request}")
        result = handler_a.handle(request)
        if result:
            print(result)
