import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Мастер и Маргарита')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', [
        '',
        'a' * 41
    ])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    @pytest.mark.parametrize('genre', [
        'Фантастика',
        'Комедии',
        'Мультфильмы'
    ])
    def test_get_books_with_specific_genre(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)

        assert collector.get_books_with_specific_genre(genre) == ['Книга']

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Детективы')

        assert collector.get_books_genre() == {
            'Книга': 'Детективы'
        }

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Фантастика для детей')
        collector.add_new_book('Детектив для взрослых')
        collector.set_book_genre('Фантастика для детей', 'Фантастика')
        collector.set_book_genre('Детектив для взрослых', 'Детективы')

        assert collector.get_books_for_children() == ['Фантастика для детей']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')

        assert collector.get_list_of_favorites_books() == ['Любимая книга']

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')

        assert collector.get_list_of_favorites_books() == ['Любимая книга']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        collector.delete_book_from_favorites('Любимая книга')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')

        assert collector.get_list_of_favorites_books() == [
            'Книга 1',
            'Книга 2'
        ]