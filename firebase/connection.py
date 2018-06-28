import datetime
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

    def insert_recent_sprint_metrics(self, json_sprint_metrics):
        try:
            self.firebase.post('/recent_sprints', json_sprint_metrics)
        except TypeError as error:
            print error


SECRET = 
DSN = 
EMAIL = 

myConn = ConnectionFirebase(SECRET, DSN, EMAIL)
myConn.connect_to_firebase()
sprint_metric = {
            'report_name': 'Sprint 1',
            'platform': 'ios',
            'unit_test_coverage': '40',
            'functional_coverage': '45',
            'contract_coverage': '72',
            'number_endpoints': '31'
        }

myConn.insert_recent_sprint_metrics(sprint_metric)
# print myConn.firebase.get('/table', None,
#                 params={'print': 'pretty'},
#                 headers={'X_FANCY_HEADER': 'very fancy'})