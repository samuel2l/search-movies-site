import requests
params={
    't': 'Flash',
    'type': 'movie',
    'plot': 'full'

}
title = input("What move do you want to search for? ")
movie_type = input("Is it a movie,series or an episode of some show? ").lower()
plot_len = input("Long or shortened plot?").lower()
params['t'] = title
params['type'] = movie_type
params['plot'] = plot_len
url = f'https://www.omdbapi.com/?'#attach your api key
response = requests.get(url,params=params)
print(response.json())
