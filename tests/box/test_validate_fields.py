import pytest

from app.helpers.validator import is_guid_valid, validate_box_name, validate_cyrillic
from app.models.box import get_age_days
from tests.test_data.box_test_data import EXISTING_GUID


@pytest.mark.validation
def test_validate_guid_after_get(box_client):
    response = box_client.get_box(EXISTING_GUID)
    guid = response.body()['id']
    assert is_guid_valid(guid), f'Extracted GUID is not valid!. Extracted GUID: {guid}'


@pytest.mark.validation
def test_validate_name_after_get(box_client):
    response = box_client.get_box(EXISTING_GUID)
    name = response.body()['name']
    assert validate_box_name(name), f'Extracted name is not valid!. Extracted name: {name}'


@pytest.mark.validation
def test_validate_cyrillic_after_get(box_client):
    response = box_client.get_box(EXISTING_GUID)
    name = response.body()['name']
    assert validate_cyrillic(name), f'Extracted name is not valid!. Extracted name: {name}'


@pytest.mark.validation
def test_validate_age_days_field(box_client, box_data):
    create_response = box_client.create_box(box_data)
    guid = create_response.text()

    create_response.check_status(200)

    get_response = box_client.get_box(guid)
    expected_age_days = get_age_days(box_data['make_date'])
    actual_age_days = get_response.body()['age_days']

    assert expected_age_days == actual_age_days
