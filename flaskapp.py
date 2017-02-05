from flask import Flask, request, render_template 
from datetime import datetime
from twilio.rest import TwilioRestClient
import time
import threading

account_sid = "put account sid here"
auth_token = "put auth token here"
client = TwilioRestClient(account_sid, auth_token)

def makeAppointment(seconds, message,phonenumber):
    print('thread started')
    time.sleep(seconds)
    sendSMS(message,phonenumber)
    return None

def sendSMS(message, phonenumber):
    client.messages.create(to="+1"+str(phonenumber), from_="put phone number here",body=message)
    return None

app = Flask(__name__, static_url_path='')

#GET for setting appointment
@app.route('/')
def index():
    return app.send_static_file('landingPage.html')
        
@app.route('/makeapointment',methods=['POST'])
def appointment():
        if request.method == 'POST':
                phonenumber = request.form['phone']
                message = request.form['message']
                time = request.form['dateandtime']
                year = int(time.split('-')[0])
                day =  int(time.split('-')[2].split('T')[0])
                month = int(time.split('-')[1])
                hour = int(time.split('T')[1].split(':')[0])
                minute = int(time.split('T')[1].split(':')[1])
                date = datetime(year,month,day,hour,minute)
                # get the total seconds between the current time and time the sms is due
                difference = int((date - datetime.now()).total_seconds())
                if difference > 0:
                    t = threading.Thread(target=makeAppointment, args=(difference,message,phonenumber))
                    t.start()
                    return 'Reminder Set'
                else: 
                    return "Try again bois"
        else:
            index()
if __name__ == "__main__": app.run(host='0.0.0.0', debug=True)
