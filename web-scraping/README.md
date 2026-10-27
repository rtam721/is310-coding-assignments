## Welcome!
Hello, for my web scraping assignment, I chose to webscrape through Bulbapedia, a wiki about Pokémon. It's robots.txt allows crawling through /wiki/ pages but restricts pages like search, random-page, shipping pages, and all. Under the file, it mentions a five second crawl delay which I include between requests. My research question is:

"How did the distribution of Dragon-type Pokémon change across Generations I, II, and III?"

For my assignment, I scrape through the National Pokédex list to identify Pokémon through those generations, extract a list of dragon types, and egg groups the Pokémon are from. This could be useful to researchers or Pokémon fans if they want to find Pokémon and learn more about Dragon types. In fact my web scraping assignment could show what generations certain dragon tpye Pokémon were introduced and their characteristics.

## Bulbapedia's robots.txt file
https://bulbapedia.bulbagarden.net/robots.txt

Permits: Crawling through the basic wiki pages like /wiki/ articles

Forbids: Crawling through special pages like search, random pages, shipping, history, and other paths

Crawl delay: 5 seconds between requests

## Requirements 
Include the library and command 

pip install requests beautifulsoup4
python3 wiki_scraping.py

## More
For my assignment, I used requests to retrieve the HTML of the wiki page I chose and BeautifulSoup to find the rows I need. Through there, I filtered Dragon-type Pokémon with for loopsand if commands. I used that to extract egg groups for individual Pokemon pages and save the collected infromation in a CSV file-- dragon_pokemon.csv. From there, my scrapper found 13 Dragon type Pokémon from the first 3 generations(Pokedex #1-386)-- 3 from Gen 1, 1 from Gen 2, and 9 from Gen 3. This showed that Generation 3 had significantly more Dragon type Pokemons than tha past two. As for limitations, my egg group extraction searches links through individual pages which could give unrelated information. I also focused on the first three generations so it doesn't represent all dragon types.