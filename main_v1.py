import json
import shlex

# zoom
from pyzoom import ZoomClient

from flask import Flask, request           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")
def hello():
 return "Its Works XXS" 

@app.route("/createMeeting",methods=['POST']) 
def createMeeting():
  data = request.get_json()
  
  apiKey = "8hb7N3pVRLS5PWVrGqmOtQ"
  apiSecret = "Y4gNfLqrJnSLMlHvOfsuFXr5Tr4uMK5GRn8d"
  client = ZoomClient(apiKey, apiSecret)
  
  topic = request.form['topic']
#   start_time="2011-10-05T14:48:00.000Z"
  start_time = request.form['start_time']
  duration_min = 60
  
  response = str(client.meetings.create_meeting(
    topic, 
    start_time=start_time,
    duration_min=duration_min
    )
  )
  responses = shlex.split(response)
  
  tempAll = ""
  i = 0
  while i < 15:
    responses[i] = responses[i].replace('=', '":"', 1)
    responses[i] = '"'+responses[i]+'"'
    tempAll += str(responses[i])+","
    i += 1
  
  print('{'+str(tempAll[:-1])+'}')
  return(json.loads('{'+str(tempAll[:-1])+'}'))

@app.route("/triggerBot" ,methods=['GET']) 
def triggerBot():
  meetId = request.args.get('meetId')
  passCode = request.args.get('passCode')
  intervals = request.args.get('intervals')
  
  startBot(meetId,passCode,intervals)
  return "success"

app.run()                    # run the flask app
  