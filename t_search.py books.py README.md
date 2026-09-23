[1mdiff --git a/README.md b/README.md[m
[1mindex b22f43f..e13123d 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -8,4 +8,12 @@[m
 [m
 ## Запуск[m
 1. Скопируйте `books.json.example` в `books.json`.[m
[31m-2. Запустите скрипт: `python books.py`[m
\ No newline at end of file[m
[32m+[m[32m2. Запустите скрипт: `python books.py`[m
[32m+[m
[32m+[m[32m## Добавление книги[m
[32m+[m[32mФункция `add_book(title, author, year)` добавляет новую книгу в каталог.[m
[32m+[m[32mАвтоматически генерирует уникальный ID.[m
[32m+[m
[32m+[m[32m## Поиск по автору[m
[32m+[m[32mФункция `search_by_author(author_query)` ищет книги по частичному совпадению.[m
[32m+[m[32mРегистр не учитывается.[m
\ No newline at end of file[m
[1mdiff --git a/books.py b/books.py[m
[1mindex 2f24c20..e6494ef 100644[m
[1m--- a/books.py[m
[1m+++ b/books.py[m
[36m@@ -21,7 +21,41 @@[m [mdef display_books(books):[m
     for book in books:[m
         print(f"{book['id']:<5} | {book['title']:<30} | {book['author']:<25} | {book['year']}")[m
 [m
[32m+[m[32mdef add_book(title, author, year, filename="books.json"):[m
[32m+[m[32m    """Добавляет новую книгу в каталог."""[m
[32m+[m[32m    books = load_books(filename)[m
[32m+[m[41m    [m
[32m+[m[32m    # Генерируем новый ID[m
[32m+[m[32m    new_id = max([book["id"] for book in books], default=0) + 1[m
[32m+[m[41m    [m
[32m+[m[32m    new_book = {[m
[32m+[m[32m        "id": new_id,[m
[32m+[m[32m        "title": title,[m
[32m+[m[32m        "author": author,[m
[32m+[m[32m        "year": year[m
[32m+[m[32m    }[m
[32m+[m[41m    [m
[32m+[m[32m    books.append(new_book)[m
[32m+[m[41m    [m
[32m+[m[32m    with open(filename, "w", encoding="utf-8") as f:[m
[32m+[m[32m        json.dump(books, f, ensure_ascii=False, indent=4)[m
[32m+[m[41m    [m
[32m+[m[32m    print(f"Книга '{title}' добавлена с ID {new_id}")[m
[32m+[m
 if __name__ == "__main__":[m
     print("Добро пожаловать в Каталог книг!")[m
     books_data = load_books()[m
[31m-    display_books(books_data)[m
\ No newline at end of file[m
[32m+[m[32m    display_books(books_data)[m
[32m+[m
[32m+[m[32m    def search_by_author(author_query, filename="books.json"):[m
[32m+[m[32m    """Ищет книги по частичному совпадению с автором."""[m
[32m+[m[32m    books = load_books(filename)[m
[32m+[m[32m    results = [book for book in books if author_query.lower() in book["author"].lower()][m
[32m+[m[41m    [m
[32m+[m[32m    if not results:[m
[32m+[m[32m        print(f"Книги автора '{author_query}' не найдены")[m
[32m+[m[32m    else:[m
[32m+[m[32m        print(f"Найдено книг: {len(results)}")[m
[32m+[m[32m        display_books(results)[m
[32m+[m[41m    [m
[32m+[m[32m    return results[m
\ No newline at end of file[m
