import pytest

from tests.helpers.wrong_box_assert_helper import wrong_box_assert
from tests.test_data.box_test_data import BOXES, NOT_EXISTING_GUID, NOT_VALID_GUID


@pytest.mark.negative
@pytest.mark.parametrize('guid, status_code', ((NOT_EXISTING_GUID, 404), (NOT_VALID_GUID, 400)))
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
@pytest.mark.parametrize('guid, status_code', ((NOT_EXISTING_GUID, 404), (NOT_VALID_GUID, 400)))
def test_negative_delete_box(guid, status_code, box_client):
    response = box_client.delete_box(guid)
    response.check_status(status_code)
