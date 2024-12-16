SEARCH = 'search'


class Search:
    def __init__(self, client):
        self.client = client

    def index(self, index='items', body={}):
        return self.client.post(f"{SEARCH}/index/{index}", data=body)
