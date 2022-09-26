
from firebase_admin import credentials
cred = credentials.Certificate('cred.json')

url = 'https://home-automation-336c0-default-rtdb.firebaseio.com/'
path = {'databaseURL' : url}

import firebase_admin
firebase_admin.initialize_app(cred, path)

from firebase_admin import db
refv = db.reference('A/B/C/Switch')

while 1:
    binary = int(input('Enter 1/0 : '))
    refv.set(binary)
