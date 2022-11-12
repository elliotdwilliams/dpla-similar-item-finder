from flask import Flask
from flask import request
from flask import render_template
from dpla.api import DPLA
#from getItem import getItem
from findItem import findItem
from hubs import hubsList

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    #Get dplaId variable from the URL; blank if not found
    dplaId = request.args.get("dplaId", "")
    hub = request.args.get("hub", "")
    #if dplaId variable has a value, run the getItem script and create the title variable
    if dplaId:
        findItem(dplaId, hub)
        result1 = findItem.result1
        subject = findItem.randomSubject
        resultDisplay = findItem.resultDisplay
    #if no dplaId value, set variables to blank
    else:
        result1 = ""
        subject = ""
        resultDisplay = ""
    return (
        render_template('index.html', result1=result1, subject=subject, resultDisplay=resultDisplay, hub=hub, hubsList=hubsList)
    )

@app.route('/about')
def about():
    return render_template('about.html')
