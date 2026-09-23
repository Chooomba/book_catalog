[1mdiff --git a/README.md b/README.md[m
[1mindex e13123d..9f32c41 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -16,4 +16,8 @@[m
 [m
 ## Поиск по автору[m
 Функция `search_by_author(author_query)` ищет книги по частичному совпадению.[m
[31m-Регистр не учитывается.[m
\ No newline at end of file[m
[32m+[m[32mРегистр не учитывается.[m
[32m+[m
[32m+[m[32m## Экспорт в CSV[m
[32m+[m[32mФункция `export_books(output_filename)` экспортирует каталог в CSV файл.[m
[32m+[m[32mПо умолчанию сохраняется в `books.csv`.[m
\ No newline at end of file[m
[1mdiff --git a/books.py b/books.py[m
[1mindex e6494ef..c20c5ac 100644[m
[1m--- a/books.py[m
[1m+++ b/books.py[m
[36m@@ -58,4 +58,19 @@[m [mif __name__ == "__main__":[m
         print(f"Найдено книг: {len(results)}")[m
         display_books(results)[m
     [m
[31m-    return results[m
\ No newline at end of file[m
[32m+[m[32m    return results[m
[32m+[m
[32m+[m[32m    def export_books(output_filename="books.csv", source_filename="books.json"):[m
[32m+[m[32m    """Экспортирует каталог книг в CSV формат."""[m
[32m+[m[32m    books = load_books(source_filename)[m
[32m+[m[41m    [m
[32m+[m[32m    if not books:[m
[32m+[m[32m        print("Каталог пуст, нечего экспортировать")[m
[32m+[m[32m        return[m
[32m+[m[41m    [m
[32m+[m[32m    with open(output_filename, "w", encoding="utf-8") as f:[m
[32m+[m[32m        f.write("ID,Название,Автор,Год\n")[m
[32m+[m[32m        for book in books:[m
[32m+[m[32m            f.write(f"{book['id']},{book['title']},{book['author']},{book['year']}\n")[m
[32m+[m[41m    [m
[32m+[m[32m    print(f"Каталог экспортирован в {output_filename} ({len(books)} книг)")[m
\ No newline at end of file[m
