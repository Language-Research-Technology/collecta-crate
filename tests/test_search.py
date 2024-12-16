import pytest
from collecta_crate.endpoints.search import Search


@pytest.fixture
def mock_client(mocker):
    # Mock the client object
    return mocker.MagicMock()


@pytest.fixture
def search(mock_client):
    # Create an instance of the Search class with the mocked client
    return Search(client=mock_client)


def test_search(search, mock_client):
    # Input parameters for the method
    index = "items"
    query = {
        "bool": {
            "must": {
                "terms": {
                    "@type.keyword": [
                        "RepositoryCollection"
                    ]
                }
            }
        }
    }

    # Mocked response from the API
    mock_response = {"hits": {"total": 1, "hits": [{"_id": "123", "_source": {"name": "Test Collection"}}]}}
    mock_client.post.return_value = mock_response

    # Call the method
    result = search.index(index=index, query=query)

    # Assertions
    mock_client.post.assert_called_once_with(
        f"search/index/{index}",
        data={'query':query},
        headers={}
    )
    assert result == mock_response
