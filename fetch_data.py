import requests
import csv

api_key = '22516fbe3cc6aed2f31603c3e76064a6'

genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}'

genre_reqs = requests.get(genre_url)  
genre_data = genre_reqs.json()

genre_map = {genre['id'] : genre['name'] for genre in genre_data['genres']}

with open('movies.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'description', 'genre'])

    for page in range(1, 501):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&page={page}'
        response = requests.get(url)
        data = response.json()
        
        for movie in data['results']:
            title = movie['title']
            description = movie['overview']
            genre_list = [genre_map.get(gid) for gid in movie['genre_ids']]
            genres = ', '.join(genre_list)
            writer.writerow([title, description, genres])
