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

    def insert_current_sprint(self, json_current_sprint):
        try:
            return self.firebase.post('/sprints', json_current_sprint)
        except TypeError as error:
            print error

    def insert_sprint_metrics(self, json_sprint_metrics):
        try:
            return self.firebase.post('/metrics', json_sprint_metrics)
        except TypeError as error:
            print error

    def insert_sprint_features(self, json_sprint_features):
        try:
            return self.firebase.post('/features', json_sprint_features)
        except TypeError as error:
            print error


SECRET = 
DSN = 
EMAIL = 

myConn = ConnectionFirebase(SECRET, DSN, EMAIL)
myConn.connect_to_firebase()

sprint = {
    'name': "Sprint-01"
}

result_sprint = myConn.insert_current_sprint(sprint)

metrics = {
            'sprint_id': '-LGAmpGfcMaJ0J2F-yAy',
            'platform': 'ios',
            'unit_test_coverage': '40',
            'functional_coverage': '58',
            'contract_coverage': '72',
            'number_endpoints': '31'
        }

result_metrics = myConn.insert_sprint_metrics(metrics)

features = {
            'metrics_id': result_metrics['name'],
            'feature_name': 'Login',
            'number_scenarios_implemented': 1,
            'total_number_scenarios': 3,
            'scenarios_implemented': ['Sucesso'],
            'scenarios_not_implemented': ['Inválido', 'Alternativo'],
            'coverage': 33
}

result_features = myConn.insert_sprint_features(features)
