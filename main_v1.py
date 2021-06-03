import json
import shlex

# zoom
from pyzoom import ZoomClient
from bot import *

from flask import Flask, request           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/createMeeting") 
def createMeeting():
  data = request.get_json()
  
  apiKey = "8hb7N3pVRLS5PWVrGqmOtQ"
  apiSecret = "Y4gNfLqrJnSLMlHvOfsuFXr5Tr4uMK5GRn8d"
  client = ZoomClient(apiKey, apiSecret)
  
  response = str(client.meetings.create_meeting(
    data.topic, 
    start_time=data.star_date, 
    duration_min=60
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
  