from flask import Flask, render_template, redirect # backend stuff
import requests # get the request
from operator import itemgetter
from forms import enter   # form data
import json
app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
@app.route('/', methods=['GET', 'POST'])
def main():
  global form
  form=enter() 
  res=requests.get("https://corona.lmao.ninja/v2/countries/Burundi").json()
  if form.validate_on_submit():
  	res=requests.get("https://corona.lmao.ninja/v2/countries/"+str(form.entry.data)).json()
  if 'message' in res:     # if there is an error 
        return render_template('404.html',msg=res['message'])
  code="https://www.countryflags.io/"+res["countryInfo"]["iso2"].lower()+"/shiny/64.png"
  data="https://restcountries.eu/rest/v2/alpha?codes="+res["countryInfo"]["iso2"].lower()
  capital=requests.get(data).json()[0]["capital"]
  name=res["country"]
  flag=res["countryInfo"]["flag"]
  cases=res["cases"]
  todaycases=res["todayCases"]
  deaths=res["deaths"]
  todayDeaths=res["todayDeaths"]
  recovered=res["recovered"]
  casesPerOneMillion=res["casesPerOneMillion"]
  continent=res["continent"]
  return render_template("index.html",capital=capital,code=code,name=name,form=form,flag=flag,cases=cases,todaycases=todaycases,deaths=deaths,todayDeaths=todayDeaths,recovered=recovered,casesPerOneMillion=casesPerOneMillion,continent=continent)
@app.route('/continents', methods=['GET', 'POST'])
def continents():
    form=enter()  
    res=requests.get("https://corona.lmao.ninja/v2/continents/europe").json()
    if form.validate_on_submit():
  	   res=requests.get("https://corona.lmao.ninja/v2/continents/"+str(form.entry.data)).json()
    elif 'message' in res:     
        return render_template('404.html',msg=res['message'])
    return render_template("continents.html",form=form,name=res["continent"],cases=res["cases"],todaycases=res["todayCases"],deaths=res["deaths"],todayDeaths=res["todayDeaths"],recovered=res["recovered"],active=res["active"],critical=res["critical"])
@app.route('/news')
def news():
    res=requests.get("https://newsapi.org/v2/everything?q=Coronavirus;covid-19;quarantine&apiKey=9656a7dbfd1744f69f74e571c0223d64")
    articles=json.loads(res.content)["articles"]
    articles=sorted(articles,key=itemgetter('publishedAt'),reverse=True)
    return render_template('news.html',articles=articles)
if __name__ == '__main__':
    app.run(port=7080,debug=True)  # run on port 7080
