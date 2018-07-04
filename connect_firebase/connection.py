# -*- coding: utf-8 -*-

import datetime
import json
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

class ConnectionFirebase:
    firebase = ()
    def __init__(self, secret_key, url_storage, email):
        self.secret_key = secret_key
        self.url_storage = url_storage
        self.email = email
    
    def connect_to_firebase(self):
        try:
            authentication = FirebaseAuthentication(self.secret_key, self.email, True, True)
            self.firebase = FirebaseApplication(self.url_storage , authentication)
        except TypeError as error:
            print error

    def insert_sprint_metrics(self, json_sprint_metrics):
        try:
            return self.firebase.post('/metrics', json_sprint_metrics)
        except TypeError as error:
            print error

    def get_sprint_metrics(self):
        try:
            return self.firebase.get('/metrics', None)
        except TypeError as error:
            print error
    
    def get_sprint_metrics_by_sprint(self, sprints, sprint_name):
        json = {}
        for sprint_id in sprints:
            if sprints[sprint_id]["sprint_name"] == sprint_name:
                json = sprints[sprint_id]
        return json
        


SECRET =
DSN = 
EMAIL = 

myConn = ConnectionFirebase(SECRET, DSN, EMAIL)
myConn.connect_to_firebase()
sprint_name = "CB-Sprint-02"
sprints = myConn.get_sprint_metrics()
sprints =  json.dumps(sprints, ensure_ascii=False)
sprints = sprints.encode('utf-8', 'ignore')
with open('Sprintmetrics.json', 'w') as outfile:
    outfile.write("data = '" +  sprints+ "'")