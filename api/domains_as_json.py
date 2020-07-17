import json 
import csv

def domains_as_json():
    with open('emails.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = {}
        for row in reader:
            if row[0].split('@')[1] in data:
                data[row[0].split('@')[1]] += 1    
            else:
                data[row[0].split('@')[1]] = 1    
        
        result = []

        for key, value in data.items():
            result.append({'domain': key, 'count': value})
        for x in result:
            print(x)
        return result