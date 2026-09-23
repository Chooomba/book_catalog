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

def add_book(title, author, year, filename="books.json"):
    """Добавляет новую книгу в каталог."""
    books = load_books(filename)
    
    # Генерируем новый ID
    new_id = max([book["id"] for book in books], default=0) + 1
    
    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year
    }
    
    books.append(new_book)
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)
    
    print(f"Книга '{title}' добавлена с ID {new_id}")

def search_by_isbn(isbn, filename="books.json"):
    """Ищет книгу по точному совпадению ISBN."""
    books = load_books(filename)
    results = [book for book in books if book.get("isbn") == isbn]
    
    if not results:
        print(f"Книга с ISBN '{isbn}' не найдена")
    else:
        print(f"Найдена книга:")
        display_books(results)
    
    return results

if __name__ == "__main__":
    print("Добро пожаловать в Каталог книг!")
    books_data = load_books()
    display_books(books_data)

    def search_by_author(author_query, filename="books.json"):
    """Ищет книги по частичному совпадению с автором."""
    books = load_books(filename)
    results = [book for book in books if author_query.lower() in book["author"].lower()]
    
    if not results:
        print(f"Книги автора '{author_query}' не найдены")
    else:
        print(f"Найдено книг: {len(results)}")
        display_books(results)
    
    return results

    def export_books(output_filename="books.csv", source_filename="books.json"):
    """Экспортирует каталог книг в CSV формат."""
    books = load_books(source_filename)
    
    if not books:
        print("Каталог пуст, нечего экспортировать")
        return
    
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("ID,Название,Автор,Год\n")
        for book in books:
            f.write(f"{book['id']},{book['title']},{book['author']},{book['year']}\n")
    
    print(f"Каталог экспортирован в {output_filename} ({len(books)} книг)")


    MAX_BOOKS = 100

    MAX_BOOKS = 500
