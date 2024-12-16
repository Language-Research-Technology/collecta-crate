import pytest
from collecta_crate.endpoints.files import Files


@pytest.fixture
def mock_client(mocker):
    # Mock the client object
    return mocker.MagicMock()


@pytest.fixture
def files(mock_client):
    # Create an instance of the Files class with the mocked client
    return Files(client=mock_client)


def test_stream_file(files, mock_client):
    # Test data
    object_id = "arcp://name,hdl10.26180~23961609"
    path = "data/1-002-plain.txt"

    # Mocked response (if needed)
    mock_response = b"file content"
    mock_client.get.return_value = mock_response

    # Call the method
    result = files.stream_file(object_id=object_id, path=path)

    # Assertions
    mock_client.get.assert_called_once_with(
        "stream/arcp://name,hdl10.26180~23961609",
        {
            "id": object_id,
            "path": path
        }
    )
    assert result == mock_response