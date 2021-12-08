import pytest

from app.helpers.validator import is_guid_valid
from app.models.box import get_age_days


@pytest.mark.positive
def test_positive_get_box(box_client, expected_box_data):
    response = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    response.check_status(200)
    response.exact_body(expected_box_data)


@pytest.mark.positive
def test_positive_create_box(box_client, box_data):
    create_response = box_client.create_box(box_data)
    guid = create_response.text()
    expected_box = {'id': guid, 'name': box_data['name'],
                    'age_days': get_age_days(box_data['make_date'])}
    get_response = box_client.get_box(guid)

    create_response.check_status(200)
    assert is_guid_valid(guid), f'Extracted GUID is not valid!. Extracted GUID: {guid}'

    get_response.check_status(200)
    get_response.exact_body(expected_box)


@pytest.mark.positive
def test_positive_delete_box(box_client):
    response = box_client.delete_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    response.check_status(200)
