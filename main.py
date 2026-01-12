#!/usr/bin/env python3
"""
Главное меню для лабораторной работы №3
Порождающие паттерны проектирования
"""

import os
import sys
import importlib.util

# Добавляем src в путь Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Красивый заголовок"""
    print("╔══════════════════════════════════════════════════════════╗")
    print("║         ЛАБОРАТОРНАЯ РАБОТА №3                           ║")
    print("║      ПОРОЖДАЮЩИЕ ПАТТЕРНЫ ПРОЕКТИРОВАНИЯ                ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("👨‍💻 Автор: [Ваше имя]")
    print("👥 Группа: [Ваша группа]")
    print("📅 Дата: 2024")
    print()

def load_and_run(module_name, func_name):
    """Загрузка и запуск модуля"""
    try:
        module_path = f"src/{module_name}.py"
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if hasattr(module, func_name):
            func = getattr(module, func_name)
            func()
        else:
            print(f"❌ Функция {func_name} не найдена в {module_name}.py")
    except FileNotFoundError:
        print(f"❌ Файл {module_name}.py не найден в папке src/")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def run_all_patterns():
    """Запуск всех паттернов"""
    patterns = [
        ("🎯 SINGLETON", "singleton", "demonstrate_singleton"),
        ("🏭 FACTORY METHOD", "factory_method", "demonstrate_factory_method"),
        ("🏗️ ABSTRACT FACTORY", "abstract_factory", "demonstrate_abstract_factory"),
        ("🔨 BUILDER", "builder", "demonstrate_builder")
    ]
    
    for name, module, func in patterns:
        print(f"\n{'═' * 60}")
        print(f"{name}")
        print('═' * 60)
        load_and_run(module, func)
        
        if name != "🔨 BUILDER":
            input("\n↵ Нажмите Enter для следующего паттерна...")
            clear_screen()
            print_header()

def show_menu():
    """Отображение меню"""
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                      ГЛАВНОЕ МЕНЮ                        ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║  1. 🎯 Singleton (Одиночка)                              ║")
    print("║  2. 🏭 Factory Method (Фабричный метод)                 ║")
    print("║  3. 🏗️ Abstract Factory (Абстрактная фабрика)           ║")
    print("║  4. 🔨 Builder (Строитель)                              ║")
    print("║  5. 🚀 Запустить ВСЕ паттерны                           ║")
    print("║  0. 🚪 Выход                                            ║")
    print("╚══════════════════════════════════════════════════════════╝")

def main():
    """Основная функция"""
    clear_screen()
    print_header()
    
    while True:
        show_menu()
        
        try:
            choice = input("\n👉 Выберите опцию (0-5): ").strip()
            
            if choice == "0":
                print("\n👋 Спасибо за использование! До свидания!")
                break
            
            elif choice == "1":
                clear_screen()
                print_header()
                load_and_run("singleton", "demonstrate_singleton")
                input("\n↵ Нажмите Enter чтобы вернуться в меню...")
                clear_screen()
                print_header()
            
            elif choice == "2":
                clear_screen()
                print_header()
                load_and_run("factory_method", "demonstrate_factory_method")
                input("\n↵ Нажмите Enter чтобы вернуться в меню...")
                clear_screen()
                print_header()
            
            elif choice == "3":
                clear_screen()
                print_header()
                load_and_run("abstract_factory", "demonstrate_abstract_factory")
                input("\n↵ Нажмите Enter чтобы вернуться в меню...")
                clear_screen()
                print_header()
            
            elif choice == "4":
                clear_screen()
                print_header()
                load_and_run("builder", "demonstrate_builder")
                input("\n↵ Нажмите Enter чтобы вернуться в меню...")
                clear_screen()
                print_header()
            
            elif choice == "5":
                clear_screen()
                print_header()
                run_all_patterns()
                input("\n↵ Нажмите Enter чтобы вернуться в меню...")
                clear_screen()
                print_header()
            
            else:
                print("\n❌ Неверный выбор. Пожалуйста, введите число от 0 до 5.")
                input("↵ Нажмите Enter чтобы продолжить...")
                clear_screen()
                print_header()
        
        except KeyboardInterrupt:
            print("\n\n⚠️ Программа прервана пользователем.")
            break
        except Exception as e:
            print(f"\n❌ Неожиданная ошибка: {e}")
            input("↵ Нажмите Enter чтобы продолжить...")
            clear_screen()
            print_header()

if __name__ == "__main__":
    main()
