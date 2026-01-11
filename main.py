import strategy
import chain_of_responsibility
import iterator
import proxy
import bridge
import adapter

def main():
    print("=" * 50)
    print("Демонстрация паттернов проектирования")
    print("=" * 50)
    
    while True:
        print("\nВыберите паттерн для демонстрации:")
        print("1. Стратегия (Strategy)")
        print("2. Цепочка обязанностей (Chain of Responsibility)")
        print("3. Итератор (Iterator)")
        print("4. Прокси (Proxy)")
        print("5. Мост (Bridge)")
        print("6. Адаптер (Adapter)")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ")
        
        if choice == "1":
            print("\n--- Демонстрация паттерна Стратегия ---")
            data = [64, 34, 25, 12, 22, 11, 90]
            sorter = strategy.Sorter()
            
            sorter.set_strategy(strategy.BubbleSortStrategy())
            result = sorter.execute_sort(data)
            print(f"Результат пузырьковой сортировки: {result}")
            
            sorter.set_strategy(strategy.QuickSortStrategy())
            result = sorter.execute_sort(data)
            print(f"Результат быстрой сортировки: {result}")
            
        elif choice == "2":
            print("\n--- Демонстрация паттерна Цепочка обязанностей ---")
            handler_a = chain_of_responsibility.ConcreteHandlerA()
            handler_b = chain_of_responsibility.ConcreteHandlerB()
            handler_c = chain_of_responsibility.ConcreteHandlerC()
            
            handler_a.set_next(handler_b).set_next(handler_c)
            
            test_request = input("Введите запрос (A, B, C или другой): ")
            result = handler_a.handle(test_request)
            if result:
                print(f"Результат: {result}")
            else:
                print("Запрос не был обработан")
                
        elif choice == "3":
            print("\n--- Демонстрация паттерна Итератор ---")
            collection = iterator.BookCollection()
            collection.add_book(iterator.Book("Война и мир"))
            collection.add_book(iterator.Book("Преступление и наказание"))
            collection.add_book(iterator.Book("Мастер и Маргарита"))
            collection.add_book(iterator.Book("1984"))
            
            print("Книги в коллекции:")
            for i, book in enumerate(collection, 1):
                print(f"{i}. {book}")
                
        elif choice == "4":
            print("\n--- Демонстрация паттерна Прокси ---")
            real_subject = proxy.RealSubject()
            proxy_instance = proxy.Proxy(real_subject)
            
            import time
            print("Первый запрос (кэшируется):")
            result1 = proxy_instance.request()
            print(f"Результат: {result1}")
            
            print("\nВторой запрос через 2 секунды (из кэша):")
            time.sleep(2)
            result2 = proxy_instance.request()
            print(f"Результат: {result2}")
            
        elif choice == "5":
            print("\n--- Демонстрация паттерна Мост ---")
            tv = bridge.TV()
            radio = bridge.Radio()
            
            remote_tv = bridge.RemoteControl(tv)
            remote_radio = bridge.AdvancedRemoteControl(radio)
            
            print("Управление TV:")
            remote_tv.toggle_power()
            remote_tv.volume_up()
            remote_tv.volume_up()
            
            print("\nУправление Radio:")
            remote_radio.toggle_power()
            remote_radio.volume_up()
            remote_radio.mute()
            
        elif choice == "6":
            print("\n--- Демонстрация паттерна Адаптер ---")
            european_socket = adapter.EuropeanSocket()
            kettle = adapter.AmericanKettle(1500)
            
            print("Создан адаптер для американского чайника")
            socket_adapter = adapter.SocketAdapter(european_socket)
            kettle.plug = socket_adapter
            
            if kettle.boil():
                print("Чайник успешно вскипятил воду!")
            else:
                print("Ошибка при кипячении воды")
                
        elif choice == "0":
            print("Выход из программы...")
            break
            
        else:
            print("Неверный выбор. Попробуйте еще раз.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
