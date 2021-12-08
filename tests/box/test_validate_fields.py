import pytest

from app.helpers.validator import is_guid_valid, validate_box_name, validate_cyrillic


@pytest.mark.validation
def test_validate_guid_after_get(box_client):
    response = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    guid = response.body()['id']
    assert is_guid_valid(guid), f'Extracted GUID is not valid!. Extracted GUID: {guid}'


@pytest.mark.validation
def test_validate_name_after_get(box_client):
    response = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    name = response.body()['name']
    assert validate_box_name(name), f'Extracted name is not valid!. Extracted name: {name}'


@pytest.mark.validation
def test_validate_cyrillic_after_get(box_client):
    response = box_client.get_box('2f11868c-a367-48dc-b4d1-c6706f5258f4')
    name = response.body()['name']
    assert validate_cyrillic(name), f'Extracted name is not valid!. Extracted name: {name}'
