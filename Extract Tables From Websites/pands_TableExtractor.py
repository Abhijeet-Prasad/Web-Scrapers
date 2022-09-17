import pandas as pd

url = 'https://en.wikipedia.org/wiki/Lists_of_One_Piece_episodes'

tables = pd.read_html(url)      # Extracts All the Table from the page. But be need only the first table at index 0.
tables[0].to_excel('One Piece Episodes List.xlsx')