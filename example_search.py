from collecta_crate.collecta import Collecta

client = Collecta("https://data.ldaca.edu.au/api", api_key="your_api_key_here")

items = client.search.index(
    index='items',
    query={
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
)
print(items)

