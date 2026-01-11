"""
Factory Method Pattern (Фабричный метод)
Определяет интерфейс для создания объекта
"""

from abc import ABC, abstractmethod
from enum import Enum


class DocumentType(Enum):
    """Типы документов"""
    PDF = "pdf"
    WORD = "word"
    EXCEL = "excel"


class Document(ABC):
    """
    Абстрактный Продукт: Документ
    """
    
    @abstractmethod
    def open(self) -> str:
        """Открыть документ"""
        pass
    
    @abstractmethod
    def save(self) -> str:
        """Сохранить документ"""
        pass
    
    @abstractmethod
    def print(self) -> str:
        """Распечатать документ"""
        pass


class PDFDocument(Document):
    """
    Конкретный Продукт: PDF документ
    """
    
    def __init__(self, filename: str):
        self.filename = filename
    
    def open(self) -> str:
        return f"📄 Открываю PDF документ: {self.filename}"
    
    def save(self) -> str:
        return f"💾 Сохраняю PDF: {self.filename}"
    
    def print(self) -> str:
        return f"🖨️ Печатаю PDF: {self.filename}"
    
    def __str__(self):
        return f"PDFDocument({self.filename})"


class WordDocument(Document):
    """
    Конкретный Продукт: Word документ
    """
    
    def __init__(self, filename: str):
        self.filename = filename
    
    def open(self) -> str:
        return f"📝 Открываю Word документ: {self.filename}"
    
    def save(self) -> str:
        return f"💾 Сохраняю Word: {self.filename}"
    
    def print(self) -> str:
        return f"🖨️ Печатаю Word: {self.filename}"
    
    def __str__(self):
        return f"WordDocument({self.filename})"


class ExcelDocument(Document):
    """
    Конкретный Продукт: Excel документ
    """
    
    def __init__(self, filename: str):
        self.filename = filename
    
    def open(self) -> str:
        return f"📊 Открываю Excel документ: {self.filename}"
    
    def save(self) -> str:
        return f"💾 Сохраняю Excel: {self.filename}"
    
    def print(self) -> str:
        return f"🖨️ Печатаю Excel: {self.filename}"
    
    def __str__(self):
        return f"ExcelDocument({self.filename})"


class DocumentCreator(ABC):
    """
    Абстрактный Создатель
    """
    
    @abstractmethod
    def create_document(self, filename: str) -> Document:
        """Фабричный метод"""
        pass
    
    def process_document(self, filename: str) -> list:
        """
        Бизнес-логика, использующая фабричный метод
        """
        document = self.create_document(filename)
        steps = [
            f"1. {document.open()}",
            f"2. {document.save()}",
            f"3. {document.print()}"
        ]
        return steps


class PDFCreator(DocumentCreator):
    """
    Конкретный Создатель для PDF
    """
    
    def create_document(self, filename: str) -> Document:
        return PDFDocument(filename)
    
    def creator_info(self) -> str:
        return "📄 PDF Creator - специализируется на PDF документах"


class WordCreator(DocumentCreator):
    """
    Конкретный Создатель для Word
    """
    
    def create_document(self, filename: str) -> Document:
        return WordDocument(filename)
    
    def creator_info(self) -> str:
        return "📝 Word Creator - специализируется на Word документах"


class ExcelCreator(DocumentCreator):
    """
    Конкретный Создатель для Excel
    """
    
    def create_document(self, filename: str) -> Document:
        return ExcelDocument(filename)
    
    def creator_info(self) -> str:
        return "📊 Excel Creator - специализируется на Excel документах"


class DocumentFactory:
    """
    Фабрика фабрик
    """
    
    @staticmethod
    def get_creator(doc_type: DocumentType) -> DocumentCreator:
        creators = {
            DocumentType.PDF: PDFCreator(),
            DocumentType.WORD: WordCreator(),
            DocumentType.EXCEL: ExcelCreator()
        }
        return creators[doc_type]


def demonstrate_factory_method():
    """Демонстрация работы Factory Method"""
    print("\n" + "=" * 60)
    print("🎯 ДЕМОНСТРАЦИЯ FACTORY METHOD (Фабричный метод)")
    print("=" * 60)
    
    # Создаём документы разных типов
    print("\n1. Создаём PDF документ:")
    pdf_creator = DocumentFactory.get_creator(DocumentType.PDF)
    print(f"   {pdf_creator.creator_info()}")
    pdf_steps = pdf_creator.process_document("report.pdf")
    for step in pdf_steps:
        print(f"   {step}")
    
    print("\n2. Создаём Word документ:")
    word_creator = DocumentFactory.get_creator(DocumentType.WORD)
    print(f"   {word_creator.creator_info()}")
    word_steps = word_creator.process_document("essay.docx")
    for step in word_steps:
        print(f"   {step}")
    
    print("\n3. Создаём Excel документ:")
    excel_creator = DocumentFactory.get_creator(DocumentType.EXCEL)
    print(f"   {excel_creator.creator_info()}")
    excel_steps = excel_creator.process_document("budget.xlsx")
    for step in excel_steps:
        print(f"   {step}")
    
    print("\n" + "=" * 60)
    print("✅ FACTORY METHOD: Создание объектов без указания конкретных классов!")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_factory_method()
