from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверяем, что нельзя добавить дубликат
    def test_add_new_book_duplicate_name(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Гордость и предубеждение и зомби")
        assert len(collector.get_books_genre()) == 1

    # проверяем, что книга с пустым именем не добавляется
    def test_add_new_book_with_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.get_books_genre().keys()

    # проверяем что книги с возрастным рейтингом отсутствуют в списке книг для детей
    def test_get_books_for_children_no_adult_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # Устанавливаем жанр книги как 'Ужасы', который считается недопустимым для детей
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_books_for_children()

    # проверяем, что нельзя присвоить книге невалидный жанр
    def test_set_book_genre_with_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фентези')
        assert '' in collector.get_book_genre('Что делать, если ваш кот хочет вас убить') 

    # проверяем что книге можно присвоить валидный жанр
    def test_get_book_genre_with_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') is 'Ужасы'

    # проверяем что выводится список книг по жанру
    def test_get_books_with_specific_genre_with_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert 'Что делать, если ваш кот хочет вас убить' and 'Гордость и предубеждение и зомби' in collector.get_books_with_specific_genre('Ужасы')

    # проверяем, что можно получить словарь с добавленными книгами
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        
        expected_genre_dict = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Комедии'
        }
        assert collector.get_books_genre() == expected_genre_dict

    # проверяем, что можно добавить книгу в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites

    # проверяем, что можно удалить книгу из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == []

    # проверяем, что можно получить список Избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()