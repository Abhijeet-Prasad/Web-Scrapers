from bs4 import BeautifulSoup
import requests
import openpyxl

excelFile = openpyxl.Workbook()
activeSheet = excelFile.active
activeSheet.title = "IMDB Top Rated Movies"

activeSheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])

url = "https://www.imdb.com/chart/top"

try:
    data = requests.get(url)
    data.raise_for_status()     # Raise Exception when site is not found

    soup = BeautifulSoup(data.text, 'html.parser')
    movie_list = soup.find('tbody', class_='lister-list')

    for tr in movie_list.find_all('tr'):
        movieName = tr.find('td', class_="titleColumn").a.text
        movieRank = tr.find('td', class_="titleColumn").text.split('.')[0]
        releaseYear = tr.find('td', class_="titleColumn").span.text.strip('()')
        movieRating = tr.find('td', class_="ratingColumn").strong.text
        #print(movieRank, movieName, releaseYear, movieRating)
        activeSheet.append([movieRank, movieName, releaseYear, movieRating])
    excelFile.save('IMDB Movie Ratings.xlsx')
except Exception as e:
    print(e)

