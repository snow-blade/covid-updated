from flask import Flask, render_template, redirect # backend stuff
import requests # get the request
from operator import itemgetter
from forms import enter   # form data
import json
class routes():
    def continents():
        form=enter()  
        #--- get request
        res=requests.get("https://corona.lmao.ninja/v2/continents/europe").json() # get the continent data
        if form.validate_on_submit():
              res=requests.get("https://corona.lmao.ninja/v2/continents/"+str(form.entry.data)).json() #if the client entered data
        #----error handling
        elif 'message' in res:     
           return render_template('404.html',msg=res['message'])
        #--rendering
        return render_template("continents.html",form=form,name=res["continent"],cases=res["cases"],todaycases=res["todayCases"],deaths=res["deaths"],todayDeaths=res["todayDeaths"],recovered=res["recovered"],active=res["active"],critical=res["critical"])

    
    def main():
        form=enter()  # get the form data
        res=requests.get("https://corona.lmao.ninja/v2/countries/Burundi").json()
        #--- form data
        if form.validate_on_submit():
            res=requests.get("https://corona.lmao.ninja/v2/countries/"+str(form.entry.data)).json() # if the user made a search, then use this data as the data to be displayed
        #---error handling
        if 'message' in res:     # if there is an error 
             return render_template('404.html',msg=res['message'])  # print it in the 404 template
        #---varibles
        code="https://www.countryflags.io/"+res["countryInfo"]["iso2"].lower()+"/shiny/64.png"  # get the shiny flag from countryflags api 
        data="https://restcountries.eu/rest/v2/alpha?codes="+res["countryInfo"]["iso2"].lower()  # get the country info from restcountries
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
        #---return statement
        return render_template("index.html",capital=capital,code=code,name=name,form=form,flag=flag,cases=cases,todaycases=todaycases,deaths=deaths,todayDeaths=todayDeaths,recovered=recovered,casesPerOneMillion=casesPerOneMillion,continent=continent) # render the template
   

    def news():
        res=requests.get("https://newsapi.org/v2/everything?q=Coronavirus;covid-19;quarantine&apiKey=your_key") # get news from the news API
        articles=json.loads(res.content)["articles"] # get the articles
        articles=sorted(articles,key=itemgetter('publishedAt'),reverse=True) #sort by date
        return render_template('news.html',articles=articles)
