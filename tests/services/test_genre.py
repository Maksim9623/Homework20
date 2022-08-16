import pytest
from unittest.mock import MagicMock

from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture
def genre_dao():
    dao = GenreDAO(None)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

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

    @pytest.mark.parametrize('mid, genre', parameters)
    def test_get_one(self, mid, genre):
        self.genre_service.dao.get_one.return_value = genre
        assert self.genre_service.get_one(mid) == genre, 'BAD'

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

    @pytest.mark.parametrize('genre', parameters)
    def test_get_all(self, genre):
        self.genre_service.dao.get_all.return_value = genre
        assert self.genre_service.get_all() == genre, 'BAD'

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

    @pytest.mark.parametrize('genre', parameters)
    def test_create(self, genre):
        self.genre_service.dao.create.return_value = genre
        assert self.genre_service.create(genre) == genre, 'BAD'

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

    @pytest.mark.parametrize('genre_old, genre_new', parameters)
    def test_update(self, genre_old, genre_new):
        self.genre_service.dao.update.return_value = genre_new
        assert self.genre_service.update(genre_new) == genre_new, 'BAD'

    def test_delete(self):
        self.genre_service.delete(1)
        self.genre_service.dao.delete.assert_called_once_with(1)
