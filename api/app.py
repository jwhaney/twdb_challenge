from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import csv, json
import os 
from os import path
from emails_as_json import emails_as_json

app = Flask(__name__)

@app.route('/')
def return_all():
    return emails_as_json()

@app.route('/domains')
def return_unique_domains():
    #find all unique domains
    
    return {}

if __name__ == "__main__":
        app.run(debug=True)