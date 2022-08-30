import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask.helpers import send_file
from jinja2 import Template

import matplotlib.pyplot as plt
from os import path
import re
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
model = pickle.load(open('nb_model2.pkl', 'rb'))
model = pickle.load(open('dt_model2.pkl', 'rb')) 

#------------------------------ Launcing undex page-------------------------------------------
@app.route('/')

def index():
    return render_template('index.html')



#------------------------------About us-------------------------------------------
@app.route('/aboutusnew')
def aboutusnew():
    return render_template('aboutusnew.html')





@app.route('/index2')
def index2():
  
    return render_template("index2.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    _Airline = float(request.args.get('_Airline'))
    _Flight = float(request.args.get('_Flight'))
    AirportFrom  = float(request.args.get('AirportFrom'))
    AirportTo = float(request.args.get('AirportTo'))
    _Dayofweek =float(request.args.get('_Dayofweek'))
    _Time = float(request.args.get('_Time'))
    Length = float(request.args.get('Length'))
    
    prediction = model.predict([[_Airline, _Flight,  AirportFrom , AirportTo,_Dayofweek,_Time,Length]])
    if prediction==1:
      pre="Flight is Delay"
    else:
      pre="Flight is not Delay"
    return pre

    return render_template('index2.html', prediction_text=pre )
   
if __name__ == "__main__":
    app.run(debug=True)
   
