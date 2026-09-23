import json
from books import search_by_author, load_books

def test_search_by_author():
    # Создаем тестовые данные
    test_data = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1869},
        {"id": 2, "title": "Анна Каренина", "author": "Лев Толстой", "year": 1877},
        {"id": 3, "title": "Преступление и наказание", "author": "Федор Достоевский", "year": 1866}
    ]
    
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=4)
    
    # Ищем книги Толстого
    results = search_by_author("Толстой")
    
    assert len(results) == 2
    assert all(book["author"] == "Лев Толстой" for book in results)
    print(f"✓ Тест поиска пройден: найдено {len(results)} книг")

if __name__ == "__main__":
    test_search_by_author()