from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField


class SearchMovie(FlaskForm):
    # Define the SelectField with options
    title = StringField(label = 'title')
    movie_type = SelectField('type', choices=[
        ('movie', 'movie'),
        ('episode', 'episode'),
        ('series', 'series')
    ])
    length = SelectField('plot length', choices=[
        ('short', 'short'),
        ('full', 'full')
    ])
    submit = SubmitField('Search')
