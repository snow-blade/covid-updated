from flask import Flask, render_template, redirect # backend stuff
import requests # get the request
from forms import enter   # form data
app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
@app.route('/', methods=['GET', 'POST'])
def main():
  form=enter() 
  res=requests.get("https://corona.lmao.ninja/v2/countries/Burundi").json()
  if form.validate_on_submit():
  	res=requests.get("https://corona.lmao.ninja/v2/countries/"+str(form.entry.data)).json()
  if 'message' in res:     # if there is an error 
        return render_template('404.html',msg=res['message'])
  flag=res["countryInfo"]["flag"]
  cases=res["cases"]
  todaycases=res["todayCases"]
  deaths=res["deaths"]
  todayDeaths=res["todayDeaths"]
  recovered=res["recovered"]
  casesPerOneMillion=res["casesPerOneMillion"]
  continent=res["continent"]
  return render_template("index.html",form=form,flag=flag,cases=cases,todaycases=todaycases,deaths=deaths,todayDeaths=todayDeaths,recovered=recovered,casesPerOneMillion=casesPerOneMillion,continent=continent)

if __name__ == '__main__':
    app.run(port=7080,debug=True)  # run on port 7080
