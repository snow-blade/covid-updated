from flask import Flask, render_template, redirect # backend stuff
import requests # get the request
from operator import itemgetter
from forms import enter   # form data
import json
from routes import routes
app=Flask(__name__)
app.config['SECRET_KEY'] = 'your_key'
@app.route('/', methods=['GET', 'POST'])
def main():
  return routes.main()
@app.route('/continents', methods=['GET', 'POST'])
def continents():
  return routes.continents()
@app.route('/news')
  return routes.news()
if __name__ == '__main__':
    app.run(port=7080,debug=True)  # run on port 7080
