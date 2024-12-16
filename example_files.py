from rocrate_abstract.rocrate_abstract import Crate, minimal_crate
from collecta_crate.collecta import Collecta
from utils import download_file
from urllib.parse import urlparse, parse_qs
from pathlib import Path


BASE_PROFILE = 'https://w3id.org/ldac/profile'

client = Collecta("https://data.ldaca.edu.au/api", api_key="your_api_key_here")

results = client.search.index(
    index='items',
    body={
        "query": {
            "bool": {
                "filter": [
                    {
                        "terms": {
                            "@type.keyword": [
                                "RepositoryCollection"
                            ]
                        }
                    },
                    {
                        "terms": {
                            "_isTopLevel.@value.keyword": [
                                "true"
                            ]
                        }
                    },
                    {
                        "terms": {
                            "_root.name.@value.keyword": [
                                "Farms to Freeways Example Dataset"
                            ]
                        }
                    }
                ]
            }
        }
    }

)

f2f = results['hits']['hits']

if len(results['hits']['hits']) == 0:
    print("not found")
else:
    f2f_id = f2f[0]['_source']['@id']
    json_crate = client.objects.get_rocrate(f2f_id, with_remote_uri=True)

    rocrate = Crate(json_crate)
    root = rocrate.root()
    for part in root.props['hasPart']:
        print(f"{part['@id']}")
        parsed_url = urlparse(part['@id'])
        query_params = parse_qs(parsed_url.query)
        path = query_params.get("path", [None])[0]
        if path:
            save_path = Path('example-data') / path
            download_file(part['@id'], save_path=save_path )
