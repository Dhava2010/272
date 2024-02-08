from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID = 'ACdf1ec14d5628599bb6201619927750c8'
    TWILIO_SYNC_SERVICE_SID = ' IS08458bec6e3647e1333b51266c1422a9' 
    TWILIO_API_KEY = 'SKd132e020fbda4257b06f91f1a6abd9d6' 
    TWILIO_API_SECRET = 'nhid4oItz2C1KeiubAJ5Dj9dRjIEL1FN'


    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(port=5001)

