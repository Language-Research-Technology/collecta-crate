from collecta_crate.collecta import Collecta

client = Collecta("https://data.ldaca.edu.au/api", api_key="your_api_key_here")

### Find Repository Collections

items = client.search.index(
    index='items',
    body={
        "query": {
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
    }
)
print(items)

### Find csvs from farms to freeways

body = {
    "query": {
        "bool": {
            "filter": [
                {
                    "terms": {
                        "encodingFormat.@value.keyword": [
                            "text/csv"
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
            ],
            "must":{
                "multi_match": {
                    "query": "flood",
                    "fields": [
                        "name.@value",
                        "description.@value",
                        "inLanguage.name.@value",
                        "_text"
                    ],
                    "type": "best_fields"
                }
            }
        }
    },
    "size": 40,
    "from": 0,
    "track_total_hits": True
}

## Search all CSVs that have 'flood' in the text
items = client.search.index(
    index='items',
    body=body
)

## Print total
print(f"Total : {items['hits']['total']['value']}")
# Print name and Id
for item in items['hits']['hits']:
    print(f"{item['_source']['name']}: {item['_source']['@id']}")
