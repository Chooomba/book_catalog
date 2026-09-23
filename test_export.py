import json
import os
from books import export_books, load_books

def test_export_books():
    # Создаем тестовые данные
    test_data = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1869}
    ]
    
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=4)
    
    # Экспортируем в CSV
    export_books("books.csv")
    
    # Проверяем, что файл создан
    assert os.path.exists("books.csv")
    
    # Проверяем содержимое
    with open("books.csv", "r", encoding="utf-8") as f:
        content = f.read()
        assert "Война и мир" in content
        assert "Лев Толстой" in content
    
    print("✓ Тест экспорта пройден")
    
    # Удаляем тестовый файл
    os.remove("books.csv")

if __name__ == "__main__":
    test_export_books()