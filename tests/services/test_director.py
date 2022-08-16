import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

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

    @pytest.mark.parametrize('mid, director', parameters)
    def test_get_one(self, mid, director):
        self.director_service.dao.get_one.return_value = director
        assert self.director_service.get_one(mid) == director, 'BAD'

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

    @pytest.mark.parametrize('director', parameters)
    def test_get_all(self, director):
        self.director_service.dao.get_all.return_value = director
        assert self.director_service.get_all() == director, 'BAD'

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

    @pytest.mark.parametrize('director', parameters)
    def test_create(self, director):
        self.director_service.dao.create.return_value = director
        assert self.director_service.create(director) == director, 'BAD'

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

    @pytest.mark.parametrize('director_old, director_new', parameters)
    def test_update(self, director_old, director_new):
        self.director_service.dao.update.return_value = director_new
        assert self.director_service.update(director_new) == director_new, 'BAD'

    def test_delete(self):
        self.director_service.delete(1)
        self.director_service.dao.delete.asscert_called_once_with(1)
        