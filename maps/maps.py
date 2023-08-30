from typing import Union
from functools import partial, reduce


class MapExercise:
    @staticmethod
    def has_required_elems_number(
        row: dict, field: str, required_elem_number: int, sep: str = ","
    ) -> bool:
        """
        Проверка на наличие указанного количество элементов в строке.

        :param row: Фильтруемый объект
        :param field: Фильтруемое поле
        :param required_elem_number: Требуемое количество объектов в поле
        :param sep: Разделитель объектов
        :return: возвращает True в случае, если количество объектов разделенных через sep
        больше или равно required_elem_number
        """
        elem_number = 0
        if row[field] != "":
            elem_number = reduce(
                lambda elem_number, symbol: elem_number + 1 if symbol == sep else elem_number,
                row[field],
                1,
            )
        return elem_number >= required_elem_number

    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        filtered_movies = filter(
            partial(MapExercise.has_required_elems_number, field="country", required_elem_number=2),
            list_of_movies,
        )
        rating_of_filtered_movies = list(
            map(
                lambda row: float(row["rating_kinopoisk"]) if row["rating_kinopoisk"] else 0,
                filtered_movies,
            )
        )
        rating_of_filtered_movies = list(
            filter(lambda rating: rating > 0, rating_of_filtered_movies)
        )

        rating_sum = reduce(
            lambda rating_sum, rating: rating_sum + rating, rating_of_filtered_movies
        )
        return rating_sum / len(rating_of_filtered_movies)

    @staticmethod
    def count_symbols(obj: dict, counted_symbol: str) -> int:
        symbols_count = reduce(
            lambda symbols_number, symbol: symbols_number + 1
            if symbol == counted_symbol
            else symbols_number,
            obj["name"],
            0,
        )
        return symbols_count

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        filtered_movies = filter(
            lambda row: row["rating_kinopoisk"] and float(row["rating_kinopoisk"]) >= rating,
            list_of_movies,
        )

        if not filtered_movies:
            return 0

        symbols_count = reduce(
            lambda sum_symbols, x: sum_symbols + x,
            map(partial(MapExercise.count_symbols, counted_symbol="и"), filtered_movies),
            0,
        )
        return symbols_count
