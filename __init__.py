from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/contact')
def MaPremiereAPI():
  return render_template("contact.html")

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def histogramme():
   return render_template("histogramme.html")

@app.route("/commits/")
def commits():
    # Récupérer les données des commits depuis l'API GitHub
    url = 'https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits'
    response = requests.get(url)
    commits_data = response.json()

    # Extraire les informations nécessaires pour le graphe
    dates = []
    commit_counts = []

    for commit in commits_data:
        dates.append(commit['commit']['author']['date'])
        commit_counts.append(1)

    # Créer le graphe
    trace = go.Scatter(x=dates, y=commit_counts, mode='lines', name='Commits')
    layout = go.Layout(title='Commits over time', xaxis=dict(title='Date'), yaxis=dict(title='Number of Commits'))
    fig = go.Figure(data=[trace], layout=layout)

    # Convertir le graphe en code HTML
    graph_html = fig.to_html(full_html=False)
    return render_template("commit.html")
  
if __name__ == "__main__":
  app.run(debug=True)