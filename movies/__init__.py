from flask import Flask, render_template, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bk94334098284g6'
from movies import routes
