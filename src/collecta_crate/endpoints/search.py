SEARCH = 'search'


class Search:
    def __init__(self, client):
        self.client = client

    def index(self, index='items', query={}, headers={}):
        data = {
            'query': query
        }
        return self.client.post(f"{SEARCH}/index/{index}", data=data, headers=headers)
