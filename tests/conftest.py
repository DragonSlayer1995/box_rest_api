import pytest

from tests.box_client import BoxClient


@pytest.fixture(scope='session')
def box_client():
    return BoxClient('http://127.0.0.1:5000/')


@pytest.fixture(scope='session')
def expected_box_data():
    return {'age_days': 12, 'id': '2f11868c-a367-48dc-b4d1-c6706f5258f4', 'name': 'просто коробка'}


@pytest.fixture(scope='session')
def box_data():
    return {'name': 'Коробка ВЕЛИКОЛЕПНАЯ Номер 999', 'make_date': '2021-10-15'}
