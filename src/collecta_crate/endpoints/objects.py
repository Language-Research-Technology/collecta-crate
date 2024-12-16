OBJECTS = 'object'


class Objects:
    def __init__(self, client):
        self.client = client

    def _get_object(self, object_id=None, member_of=None, conforms_to=None, offset=0, limit=100):
        params = {
            'id': object_id,
            'memberOf': member_of,
            'conformsTo': conforms_to,
            'offset': offset,
            'limit': limit
        }
        return self.client.get(f"{OBJECTS}", params=params)

    # what is types!!??
    def _get_object_meta(self, object_id, resolve_parts, noUrid=False):
        params = {
            'id': object_id,
            'resolve_parts': resolve_parts
        }
        if noUrid:
            params.update({'noUrid': noUrid})

        return self.client.get(f"{OBJECTS}/meta/", params)

    def get_zip(self, object_id):
        return self.client.get(f"{OBJECTS}/{object_id}.zip")

    def get_all_top_level_collections(self, conforms_to, offset=0, limit=1000):
        return self._get_object(
            None,
            None,
            conforms_to=conforms_to,
            offset=offset,
            limit=limit)

    def get_members_off(self, member_of, conforms_to, offset=0, limit=1000):
        return self._get_object(
            object_id=None,
            member_of=member_of,
            conforms_to=conforms_to,
            offset=offset,
            limit=limit
        )

    # not sure of this name
    def get_children_off(self, member_of, offset=0, limit=1000):
        return self._get_object(
            member_of=member_of,
            offset=offset,
            limit=limit
        )

    # What is this!!
    def get_root_conforms_to(self, offset=0, limit=1000):
        return self._get_object(
            offset=offset,
            limit=limit
        )

    def get_rocrate(self, object_id, with_remote_uri=False):
        return self._get_object_meta(object_id=object_id, noUrid=not with_remote_uri, resolve_parts=False)

    def get_distributed_rocrate(self, object_id, with_remote_uri=False):
        return self._get_object_meta(object_id=object_id, noUrid=not with_remote_uri, resolve_parts=True)

