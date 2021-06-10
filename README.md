
# About this Repository
<img src="https://raw.githubusercontent.com/rifkyariy/ZMoodBot/master/image/logo.png" alt="Logo" width="80" height="80">

BangkitEndpoint is an API reference. This repository uses the **Flask Framework 2.0.1** and **Python 3.9**. This application can be run locally or online by deploying on the Cloud service, in the next section it is explained how to deploy this application on the **Google Cloud Platform** using the **Cloud Run** service. We configured this endpoint to be **accessible to everyone without authentication**. Configuration can be set by yourself. This applicaton 

This repository is used to predict facial expressions from images and output them in the form of several parameters according to [Facial Expression Recognition by justinshenk](https://github.com/justinshenk/fer )

And also this repository is part of Zmood App 
* [ZmoodBot](https://github.com/rifkyariy/ZMoodBot)
* [Zmood Android App](https://gitlab.com/moroartos-zmood/android-app)

## Built With
* [Flask](https://flask.palletsprojects.com/)
* [Pyzoom]([https://link](https://pypi.org/project/pyzoom/))
* [Tensorflow](https://www.tensorflow.org/)
* [OpenCV](https://opencv.org/)
* [Numpy](https://numpy.org/)
* [MTCNN](https://github.com/ipazc/mtcnn)

## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/ahsanf/BangkitEndpoint.git
    ```
2. Install Dependencies: 
    ```sh
    pip3 install -r requirements.txt
    ```
## Usages
1. Export FLASK_APP 
   * in Linux Based
      ```sh
      export FLASK_APP=main_v1.py
      ```
   * in Windows
      ```sh
      set FLASK_APP=main_v1.py
      ```

2. Run the App
   ```sh
   flask run
   ```
3. Use **/predict** route to predict your face (images) with POST method, e.g:
   ```sh
   https://localhost:5000/predict
   ```
## Output
```json
{
    "data": {
        "expression": "fear",
        "score": 0.53
    },
    "status": "success"
}
```

## Deploy To Cloud Service
### Containerizing an app and uploading it to Container Registry
To containerize the app, Dokcerfile is the configuration when it will be deployed
1. Build your container image using Cloud Build, by running the following command from the directory containing the Dockerfile:
    ```sh
    gcloud builds submit --tag gcr.io/PROJECT-ID/flaskapp
    ```
    Where PROJECT-ID is your GCP project ID. You can get it by running gcloud config get-value project.

2. Upon success, you will see a SUCCESS message containing the image name (gcr.io/PROJECT-ID/flaskapp). The image is stored in Container Registry and can be re-used if desired.

## Deploying to Cloud Run
### To deploy the container image:
1. Deploy using the following command:
    ```sh
    gcloud run deploy --image gcr.io/PROJECT-ID/flaskapp
    ```
    If prompted to enable the API, Reply **y** to enable.

    Replace PROJECT-ID with your GCP project ID. You can view your project ID by running the command ***gcloud config get-value project.***

      * You will be prompted for the service name: press Enter to accept the default name, **flaskapp.**
      * You will be prompted for region: select the region of your choice, for example **us-central1.**
      * You will be prompted to **allow unauthenticated** invocations: respond **y** .
    
    Then wait a few moments until the deployment is complete. On success, the command line displays the service URL.
2. Visit your deployed container by opening the service URL in a web browser.


## Credits
* [Facial Expression Recognition by justinshenk](https://github.com/justinshenk/fer)
* [Cloud Run Documentation: Build and deploy a Python service](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)