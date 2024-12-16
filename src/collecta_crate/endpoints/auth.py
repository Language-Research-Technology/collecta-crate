AUTH = 'auth'

class Auth:
    def __init__(self, client):
        self.client = client

    def get_memberships(self):
        return self.client.get(f"{AUTH}/memberships")