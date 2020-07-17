from flask import Flask, request, jsonify, json
from flask_cors import CORS
from emails_as_json import emails_as_json
from domains_as_json import domains_as_json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def return_all():
    data = jsonify(emails_as_json())
    
    return data

@app.route('/domains', methods=['GET'])
def return_unique_domains():
    #find all unique domains
    data = jsonify(domains_as_json())
    return data

if __name__ == "__main__":
        app.run(debug=True)