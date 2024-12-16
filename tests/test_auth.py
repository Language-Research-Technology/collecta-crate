import pytest
from collecta_crate.endpoints.auth import Auth


@pytest.fixture
def mock_client(mocker):
    # Mock the client object
    return mocker.MagicMock()


@pytest.fixture
def auth(mock_client):
    # Create an instance of the Auth class with the mocked client
    return Auth(client=mock_client)


def test_get_memberships(auth, mock_client):
    # Mocked response data
    mock_response = {"memberships": ["member1", "member2", "member3"]}
    mock_client.get.return_value = mock_response

    # Call the method
    result = auth.get_memberships()

    # Assertions
    mock_client.get.assert_called_once_with("auth/memberships")
    assert result == mock_response