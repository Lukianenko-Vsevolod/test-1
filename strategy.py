from abc import ABC, abstractmethod
from typing import List

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        print("Сортировка пузырьком")
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class QuickSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        print("Быстрая сортировка")
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def execute_sort(self, data: List[int]) -> List[int]:
        if not self._strategy:
            raise ValueError("Стратегия не установлена")
        return self._strategy.sort(data.copy())

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    sorter = Sorter()
    
    sorter.set_strategy(BubbleSortStrategy())
    result = sorter.execute_sort(data)
    print(f"Результат: {result}")
    
    sorter.set_strategy(QuickSortStrategy())
    result = sorter.execute_sort(data)
    print(f"Результат: {result}")
