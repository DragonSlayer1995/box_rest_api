import pytest

from tests.helpers.wrong_box_assert_helper import wrong_box_assert
from tests.test_data.box_test_data import BOXES


@pytest.mark.negative
@pytest.mark.parametrize('guid, status_code', (('2f11868c-a367-48dc-b4d1-c6706f5258f5', 404), ('2f11868c', 400)))
def test_negative_get_box(guid, status_code, box_client):
    response = box_client.get_box(guid)
    response.check_status(status_code)


@pytest.mark.negative
@pytest.mark.parametrize('box_data', BOXES)
def test_negative_create_box(box_client, box_data):
    create_response = box_client.create_box(box_data)
    text = create_response.text()
    create_response.check_status(400)
    wrong_box_assert(box_data, text)


@pytest.mark.negative
@pytest.mark.parametrize('guid, status_code', (('2f11868c-a367-48dc-b4d1-c6706f5258f5', 404), ('2f11868c', 400)))
def test_negative_delete_box(guid, status_code, box_client):
    response = box_client.delete_box(guid)
    response.check_status(status_code)
