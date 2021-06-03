# basic things
import time
import datetime
from datetime import datetime as dt
import os
import threading
# import numpy as np

# screenshooting
import pyautogui

# image processing
from PIL import Image
import cv2

# plot display
import matplotlib.pyplot as plt

# zoom
from pyzoom import ZoomClient

# date Time
todayDate = datetime.date.today()
hour = str(datetime.datetime.now())[11:13]
minute = str(datetime.datetime.now())[14:16]

# screen size
screenWidth, screenHeight = pyautogui.size()

# open zoom function
def openZoom(meetingID, password):
  # Open Zoom Via Mac Spotlight
  pyautogui.hotkey('command', 'space') 
  pyautogui.typewrite('Zoom')
  pyautogui.hotkey('enter')
  
  # Join Meeting
  time.sleep(1)
  pyautogui.hotkey('command', 'j') 
  pyautogui.typewrite(meetingID)
  pyautogui.hotkey('enter') 
  time.sleep(3)
  pyautogui.typewrite(password)
  pyautogui.hotkey('enter') 
  
def takeScreenshoot() :
  # directory Location
  DIR_NAME = "./data/raw"
  
  os.chdir(DIR_NAME) # change directory to save screenshot
  filename = str(todayDate)+'.png' 
  pyautogui.screenshot(filename)
  
  img = cv2.pyrDown(cv2.imread(filename, cv2.IMREAD_UNCHANGED))
  cropedImage = img[100:screenHeight-200, 0:screenWidth]  # crop to remove dock and top navbar
  
  cv2.imwrite(filename, cropedImage)

  return str(todayDate)+'.png'
  
def cropImage(imageInput):
  # input image
  img = cv2.pyrDown(cv2.imread(imageInput, cv2.IMREAD_UNCHANGED))

  # increase contrast and  brightness 
  alpha = 3 # contrast control (1.0-3.0)
  beta = 10 # brightness control (0-100)


  # adjusted image
  adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
  

  # threshold image
  # ret, threshed_img = cv2.threshold(cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY), 89, 255, cv2.THRESH_BINARY) # used when small box or max participant -> 25 participant
  ret, threshed_img = cv2.threshold(cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY) # used when large box or minim participant 
  
  # find contours and get the external one
  contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  maxArea = 0 # define max area of rectangle to get best match display box
  for c in contours:
    x, y, w, h = cv2.boundingRect(c) # get contour x, y, width, hight from image
    if w*h >= maxArea: # get max or biggest area so we can define limit below the max
      maxArea = w*h - (1 / 3 * w*h)

  nameIndex = 0 # define name index, used to write imagae name
  for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    if(w*h >= maxArea ):
      # draw a green rectangle to visualize the bounding rect
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
      
      # crop image inside bounding rectangle
      cropedImage = img[y:y+h, x:x+w]
      nameImage = cropedImage[h-50:h, 0:250]
      cv2.imwrite("data/processed/participantName_"+str(nameIndex)+".png", nameImage)
      cv2.imwrite("data/processed/participantFace_"+str(nameIndex)+".png", cropedImage)
      nameIndex=nameIndex+1

  # print count of contour
  print(len(contours))
  print("Done croping Image")
  
  # draw contour on image
  # cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
  
  # cv2.imshow("contours", threshed_img)
  cv2.imshow("contours", threshed_img)

  while True:
      key = cv2.waitKey(1)
      if key == 27: #ESC key to break
          break

  cv2.destroyAllWindows()

def detect_text(path):
  import os
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='vision.json'
  
  from google.cloud import vision
  import io
  
  client = vision.ImageAnnotatorClient()

  with io.open(path, 'rb') as image_file:
      content = image_file.read()

  image = vision.Image(content=content)

  response = client.text_detection(image=image)
  texts = response.text_annotations
      
  status = "fail"
  data = "Text Not Detected"
  
  if texts:
    status = "success"
    data = texts[0].description

  if response.error.message:
      raise Exception(
          '{}\nFor more info on error messages, check: '
          'https://cloud.google.com/apis/design/errors'.format(
              response.error.message))
  
  return {
    "status": status,
    "data": data
  }

stopNow = 0
def screenshootCycle():
  filename = takeScreenshoot()
  cropImage("/data/raw/"+str(filename))

def startBot(meetId, passCode, intervals = 3):
  openZoom(meetId, passCode)
  time.sleep(15)
  
  # if not stopNow: threading.Timer(intervals * 60, screenshootCycle).start()

