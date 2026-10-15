import csv
import os
from rich.console import Console
from rich.table import Table



console = Console()

table = Table(title="Music Artist Colllaborations")

table.add_column("Artist")
table.add_column("Song Title")
table.add_column("Collaborating Artist")
table.add_column("Year Released")
table.add_column("Song Genre")
table.add_column("Artist Genre")
table.add_column("Collaborating Artist Genre")

table.add_row(
    "Lady Gaga",
    "Die With A Smile",
    "Bruno Mars",
    "2024",
    "Pop",
    "Pop",
    "Pop/R&B"
)

table.add_row(
    "The Weeknd",
    "Save Your Tears (Remix)",
    "Ariana Grande",
    "2021",
    "Pop/R&B",
    "Pop/R&B",
    "Pop/R&B"
)

table.add_row(
    "Taylor Swift",
    "Bad Blood (Remix)",
    "Kendrick Lamar",
    "2015",
    "Pop",
    "Pop",
    "Hip-Hop/Rap"
)

console.print(table)

confirmed_entries = []
while True:
    artist = input("Enter the artist: ")
    song_title = input("Enter the song title: ")
    collaborating_artist = input("Enter the collaborating artist: ")
    year_released = input("Enter the year released: ")
    song_genre = input("Enter the song genre: ")
    artist_genre = input("Enter the artist genre: ")
    collaborating_artist_genre = input("Enter the collaborating artist genre: ")

    console.print(f"Artist: {artist}")
    console.print(f"Song Title: {song_title}")
    console.print(f"Collaborating Artist: {collaborating_artist}")
    console.print(f"Year Released: {year_released}")
    console.print(f"Song Genre: {song_genre}")
    console.print(f"Artist Genre: {artist_genre}")
    console.print(f"Collaborating Artist Genre: {collaborating_artist_genre}")

    confirm = input("Is this information correct? (yes/no): ")


    if confirm == "yes":
        table.add_row(
            artist,
            song_title,
            collaborating_artist,
            year_released,
            song_genre,
            artist_genre,
            collaborating_artist_genre
        )
        confirmed_entries.append([
            artist,
            song_title,
            collaborating_artist,
            year_released,
            song_genre,
            artist_genre,
            collaborating_artist_genre
        ])
        console.print("Information added to the table.")
        console.print(table)

        add_another = input("Would you like to add another collaboration? (yes/no): ")
        if add_another == "no":

            break

with open("music_collaborations.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Artist",
        "Song Title",
        "Collaborating Artist",
        "Year Released",
        "Song Genre",
        "Artist Genre",
        "Collaborating Artist Genre"
    ])
    writer.writerows(confirmed_entries)
    
file_path = os.path.abspath("music_collaborations.csv")
console.print(f"Data saved to: {file_path}")




