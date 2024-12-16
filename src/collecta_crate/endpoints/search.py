SEARCH = '/search'

class Search:
    def __init__(self, client):
        self.client = client

    def search(self, index='items', query={}):
        args = {
            'index': index,
            'query': query
        }
        return self.client.post(f"{SEARCH}", args=args)