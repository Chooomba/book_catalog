import json
from books import add_book, load_books

# Тест: добавляем книгу и проверяем, что она сохранилась
def test_add_book():
    # Очищаем файл для теста
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump([], f)
    
    # Добавляем книгу
    add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    
    # Проверяем
    books = load_books()
    assert len(books) == 1
    assert books[0]["title"] == "Мастер и Маргарита"
    print("✓ Тест добавления книги пройден")

if __name__ == "__main__":
    test_add_book()