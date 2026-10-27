import requests # retriuve info from webpage
from bs4 import BeautifulSoup
import time
import csv

dragon_pokemon= []
url= "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
headers = {"User-Agent": "is310-course-scraper/1.0 (student project; rtam7@illinois.edu)"}

response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.title.get_text())
else:
    print("Error:", response.status_code)
    raise SystemExit



tables = soup.find_all('table', class_='roundy')

for table in tables:
    rows = table.find_all('tr')

    for row in rows:
        each_cell = row.find_all('td', recursive=False)

        if any(each_cell.get_text(" ", strip=True) == "Dragon" for  each_cell in each_cell):
            # print([each_cell.get_text(" ", strip=True) for each_cell in each_cell])
            pokemon_data = [each_cell.get_text(" ", strip=True) for each_cell in each_cell]

            number_text = pokemon_data[0].replace("#", "")
            if number_text.isdigit():
                number = int(number_text)

                if number <= 151:
                    pokemon_data[1] = "Generation I"
                elif number <= 251:
                    pokemon_data[1] = "Generation II"
                elif number <= 386:
                    pokemon_data[1] = "Generation III"
                
                if number <= 386:
                    if len(pokemon_data)== 4:
                        pokemon_data.append("")

                    # Another page
                    dragon_pokemonlink = each_cell[2].find('a')

                    if dragon_pokemonlink:
                        individual_pokemon_url = "https://bulbapedia.bulbagarden.net" + dragon_pokemonlink.get('href')

                        time.sleep(5)

                        individual_response = requests.get(individual_pokemon_url, headers=headers, timeout=10)

                        if individual_response.status_code == 200:
                            dragon_soup = BeautifulSoup(individual_response.text, 'html.parser')

                            egg_groups = []
                            links = dragon_soup.find_all('a')

                            for link in links:
                                if "(Egg Group)" in link.get('title', ''):
                                    egg_group = link.get('title').replace(" (Egg Group)", "")

                                    if egg_group not in egg_groups:
                                        egg_groups.append(egg_group)

                            pokemon_data.append(", ".join(egg_groups))
                        else:
                            print("Error:", individual_response.status_code)
                            pokemon_data.append("")
                    else:
                        pokemon_data.append("")

                    dragon_pokemon.append(pokemon_data)
                    print(pokemon_data)
with open("dragon_pokemon.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Pokedex Number",
        "Generation",
        "Name",
        "Primary Type",
        "Secondary Type",
        "Egg Groups"
    ])
    writer.writerows(dragon_pokemon)

gen1= 0
gen2= 0
gen3= 0
for pokemon in dragon_pokemon:
    if pokemon[1] == "Generation I":
        gen1 += 1
    elif pokemon[1] == "Generation II":
        gen2 += 1
    elif pokemon[1] == "Generation III":
        gen3 += 1

print("Generation I:", gen1)
print("Generation II:", gen2)
print("Generation III:", gen3)


# going through another page

