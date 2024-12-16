from rocrate_abstract.rocrate_abstract import Crate, minimal_crate
from collecta_crate.collecta import Collecta

BASE_PROFILE='https://w3id.org/ldac/profile'

client = Collecta("https://data.ldaca.edu.au/api", api_key="your_api_key_here")

items = client.objects.get_all_top_level_collections(
    conforms_to=BASE_PROFILE + '#Collection',
    offset=0,
    limit=5
)
print(items['total'])

### Get one ro-crate from the first collection
collection = items['data'][0]
json_crate = client.objects.get_rocrate(collection['crateId'], with_remote_uri=False)

rocrate = Crate(json_crate)
## List things in the crate
for entity in rocrate.graph:
    print(f"{entity}")

### Print members of these collections
for item in items['data']:
    members_off = client.objects.get_members_off(
        member_of=item['crateId'],
        conforms_to=BASE_PROFILE + '#Object',
    )

    print(members_off)