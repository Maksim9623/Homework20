import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def movies_dao():
    dao = MovieDAO(None)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movies_service(self, movies_dao):
        self.movies_service = MovieService(dao=movies_dao)
    parameters = (
        (
            1,
            {
                'id': 1,
                'title': 'NoName'
            }
        ),
        (
            2,
            {
                'id': 2,
                'title': 'TestName'
            }
        ),
    )

    @pytest.mark.parametrize('mid, movie', parameters)
    def test_get_one(self, mid, movie):
        self.movies_service.dao.get_one.return_value = movie
        assert self.movies_service.get_one(mid) == movie, 'BAD'

    parameters = (
        (
            [
                1,
                {
                    'id': 1,
                    'title': 'NoName'
                },
                2,
                {
                    'id': 2,
                    'title': 'TestName'
                }
            ]
        ),
    )

    @pytest.mark.parametrize('movie', parameters)
    def test_get_all(self, movie):
        self.movies_service.dao.get_all.return_value = movie
        assert self.movies_service.get_all() == movie, 'BAD'

    parameters = (
        (
            {
                'id': 1,
                'title': 'NoName'
            }
        ),
        (
            {
                'id': 2,
                'title': 'TestName'
            }
        ),
    )

    @pytest.mark.parametrize('movie', parameters)
    def test_create(self, movie):
        self.movies_service.dao.create.return_value = movie
        assert self.movies_service.create(movie) == movie, 'BAD'

    parameters = (
            (
                {
                    'id': 1,
                    'title': 'NoName'
                },
                {
                    'id': 2,
                    'title': 'TestName'
                }
            ),
        )

    @pytest.mark.parametrize('movie_original, movie_new', parameters)
    def test_create(self, movie_original, movie_new):
        self.movies_service.dao.update.return_value = movie_new
        assert self.movies_service.dao.update(movie_new) == movie_new, 'BAD'

    def test_delete(self,):
        self.movies_service.delete(1)
        self.movies_service.dao.delete.assert_called_once_with(1)
