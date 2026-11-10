import requests 
import json

# Anilist
anime_url= "https://graphql.anilist.co"

query= """
query ($search: String) {
  Media (search: $search, type: ANIME) {
    title {
        english
        }
        seasonYear
        genres
        description
        popularity
    }
}
"""
variables = { 
    "search": "Death Note"
}
anime_title= None

try:
    response= requests.post(
        anime_url, 
        json={"query": query, "variables": variables}, 
        timeout=15
    )



    if response.status_code == 200:
        data= response.json()

        if "errors" in data:
            print("AniList GraphQL errors:", data["errors"])
        else:
            anime_info= data["data"]["Media"]
            anime_title= anime_info["title"]["english"]
            print("AniList Response: ", anime_info)

            with open("anilist_data.json", "w", encoding= "utf-8") as file:
                json.dump(anime_info, file, indent=4, ensure_ascii=False)
    else:
        print("Error:", response.status_code)

except (requests.exceptions.RequestException, ValueError, KeyError, TypeError) as error:
    print("AniList Request failed:", error)

# MediaWiki Action API
if anime_title is not None:
    wiki_url= "https://en.wikipedia.org/w/api.php"

    wiki_params= {
        "action": "query",
        "prop": "extracts",
        "exintro": 1,
        "explaintext": 1,
        "titles": anime_title,
        "format": "json",
    }

    try:
        wiki_response= requests.get(
            wiki_url, 
            params=wiki_params, 
            headers= {
                "User-Agent": "IS310-Assignment/1.0 (rtam7@illinois.edu)"
            },
            timeout=15
        )

        if wiki_response.status_code == 200:
            wiki_data= wiki_response.json()
            wiki_info= list(wiki_data["query"]["pages"].values())[0]
            print("MediaWiki Response: ", wiki_info)
            with open("mediawiki_data.json", "w", encoding="utf-8") as file:
                json.dump(wiki_info, file, indent=4,ensure_ascii=False)
        else:
            print("Error:", wiki_response.status_code)
    except (requests.exceptions.RequestException, ValueError, KeyError, TypeError, IndexError) as error:
        print("MediaWiki Request failed:", error)

