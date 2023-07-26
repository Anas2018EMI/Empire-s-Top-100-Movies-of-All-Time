from bs4 import BeautifulSoup
import requests
import json

top_movies = []
response = requests.get(
    url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")  # "lxml"
movies_titles = soup.find_all("script", type="application/json")

data = json.loads(movies_titles[0].string)
data_list = data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][3]["content"]["images"]

for title in data_list:
    top_movies += [title["titleText"]]

top_movies.reverse()
with open("Empire's Top 100 Movies of All Time.txt", mode="w") as file:
    for title in top_movies:
        file.write(title+"\n")
