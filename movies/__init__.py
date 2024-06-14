from flask import Flask, render_template, request
app = Flask(__name__)
app.config['SECRET_KEY'] = '' #insert app key here
from movies import routes
