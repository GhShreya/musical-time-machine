import requests
from bs4 import BeautifulSoup
URL = "https://www.billboard.com/charts/hot-100"
print("Travel back in time with nostalgic music!")
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(f"{URL}/{date}")
data = response.text
soup = BeautifulSoup(data, "html.parser")
all_songs = soup.select("li ul li h3")
songs = [song.getText().strip() for song in all_songs]
if len(songs) != 0:
    print("Here's the billboard tops from that era:-")
    for i in songs:
        print(i)
else:
    print("Try traveling to some other time :)")
