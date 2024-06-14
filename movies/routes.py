from flask import render_template, redirect, url_for, flash, request
from movies.forms import SearchMovie
from movies import app
import requests
# line abv is possible without doing store.__init


# USER: Samuel, password:password
@app.route("/",methods=['POST','GET'])
def home():
    form = SearchMovie()

    params = {
        't':' flash',
        'type': 'movie',
        'plot': 'full'
    }
    if request.method == 'POST':
        params['t'] = form.title.data
        params['type'] = form.movie_type.data

        print(form.title.data)
        print(form.movie_type.data)
        params['plot'] = form.length.data
        print(form.length.data)
        url = f'https://www.omdbapi.com/?apikey='#add your api key
        response = requests.get(url, params=params)
        if response.status_code == 200:

            print(response.json())

            return render_template('home.html',form=form,data=response.json())

    return render_template('home.html',form=form,data="Does not exist")