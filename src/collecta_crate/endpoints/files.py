FILES = 'stream'

class Files:
    def __init__(self, client):
        self.client = client

    def stream_file(self, object_id, path):
        params = {
            'id': object_id,
            'path': path
        }
        return self.client.get(f"{FILES}/{object_id}", params)