import json
import os

def load_books(filename="books.json"):
    """Загружает список книг из JSON файла."""
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден. Создайте его на основе books.json.example")
        return []
    
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def display_books(books):
    """Выводит список книг в консоль."""
    if not books:
        print("Каталог пуст.")
        return
        
    print(f"{'ID':<5} | {'Название':<30} | {'Автор':<25} | {'Год'}")
    print("-" * 70)
    for book in books:
        print(f"{book['id']:<5} | {book['title']:<30} | {book['author']:<25} | {book['year']}")

if __name__ == "__main__":
    print("Добро пожаловать в Каталог книг!")
    books_data = load_books()
    display_books(books_data)