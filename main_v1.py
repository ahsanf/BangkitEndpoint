import json
import shlex
import os

# zoom
from pyzoom import ZoomClient
#from bot import *

from flask import Flask, request           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")
def hello():
 return "Its Works" 

@app.route("/createMeeting") 
def createMeeting():
  data = request.get_json()
  
  apiKey = "8hb7N3pVRLS5PWVrGqmOtQ"
  apiSecret = "Y4gNfLqrJnSLMlHvOfsuFXr5Tr4uMK5GRn8d"
  client = ZoomClient(apiKey, apiSecret)
  
  topic = request.form['topic']
  start_time = request.form['start_time']
  
  response = str(
    client.meetings.create_meeting(
        topic, 
        start_time, 
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

# @app.route("/triggerBot" ,methods=['GET']) 
# def triggerBot():
#   meetId = request.args.get('meetId')
#   passCode = request.args.get('passCode')
#   intervals = request.args.get('intervals')
  
#   startBot(meetId,passCode,intervals)
#   return "success"

#app.run()                    # run the flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080))) 