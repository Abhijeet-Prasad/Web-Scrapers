import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_anime_series_by_episode_count'

tables = pd.read_html(url)

tables[1].to_excel('Anime List.xlsx')