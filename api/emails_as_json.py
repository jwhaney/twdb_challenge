import json 
import csv

def emails_as_json():
    with open('emails.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = { 'emails' : [] }
        for row in reader:
            data['emails'].append({'address': row[0]})
        
        return data