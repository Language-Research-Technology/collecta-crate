from rocrate_abstract.rocrate_abstract import Crate, minimal_crate
from collecta_crate.endpoints.objects import Objects
import pytest


@pytest.fixture
def mock_client(mocker):
    # Fixture to provide a mocked client
    return mocker.MagicMock()


@pytest.fixture
def objects(mock_client):
    # Fixture to create an instance of the Objects class
    return Objects(client=mock_client)


def test_get_object(objects, mock_client):
    objects._get_object(object_id='123', member_of='group1', conforms_to='schema', offset=0, limit=10)
    mock_client.get.assert_called_once_with(
        'object',
        params={
            'id': '123',
            'memberOf': 'group1',
            'conformsTo': 'schema',
            'offset': 0,
            'limit': 10
        }
    )


def test_get_object_meta(objects, mock_client):
    objects._get_object_meta(object_id='123', resolve_parts=True, noUrid=True)
    mock_client.get.assert_called_once_with(
        'object/meta/',
        {
            'id': '123',
            'resolve_parts': True,
            'noUrid': True
        }
    )


def test_get_zip(objects, mock_client):
    objects.get_zip(object_id='123')
    mock_client.get.assert_called_once_with('object/123.zip')


def test_get_all_top_level_collections(objects, mock_client):
    objects.get_all_top_level_collections(conforms_to='schema', offset=5, limit=10)
    mock_client.get.assert_called_once_with(
        'object',
        params={
            'id': None,
            'memberOf': None,
            'conformsTo': 'schema',
            'offset': 5,
            'limit': 10
        }
    )


def test_get_members_off(objects, mock_client):
    objects.get_members_off(member_of='group1', conforms_to='schema', offset=10, limit=20)
    mock_client.get.assert_called_once_with(
        'object',
        params={
            'id': None,
            'memberOf': 'group1',
            'conformsTo': 'schema',
            'offset': 10,
            'limit': 20
        }
    )


def test_get_children_of(objects, mock_client):
    objects.get_children_of(member_of='group1', offset=15, limit=25)
    mock_client.get.assert_called_once_with(
        'object',
        params={
            'conformsTo': None,
            'id': None,
            'memberOf': 'group1',
            'offset': 15,
            'limit': 25
        }
    )


def test_get_root_conforms_to(objects, mock_client):
    objects.get_root_conforms_to(offset=20, limit=30)
    mock_client.get.assert_called_once_with(
        'object',
        params={
            'id': None,
            'memberOf': None,
            'conformsTo': None,
            'offset': 20,
            'limit': 30
        }
    )


def test_get_rocrate(objects, mock_client):
    objects.get_rocrate(object_id='123', with_remote_uri=True)
    mock_client.get.assert_called_once_with(
        'object/meta/',
        {
            'id': '123',
            'resolve_parts': False
        }
    )


def test_get_distributed_rocrate(objects, mock_client):
    objects.get_distributed_rocrate(object_id='456', with_remote_uri=False)
    mock_client.get.assert_called_once_with(
        'object/meta/',
        {
            'id': '456',
            'resolve_parts': True,
            'noUrid': True
        }
    )
