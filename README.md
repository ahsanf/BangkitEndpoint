# About this Repository
BangkitEndpoint is an API reference. This repository uses the **Flask Framework 2.0.1** and **Python 3.8**. This application can be run locally or online by deploying on the Cloud service, in the next section it is explained how to deploy this application on the **Google Cloud Platform** using the **Cloud Run** service. We configured this endpoint to be **accessible to everyone without authentication**. Configuration can be set by yourself.

# Containerizing an app and uploading it to Container Registry
To containerize the app, Dokcerfile is the configuration when it will be deployed
1. Build your container image using Cloud Build, by running the following command from the directory containing the Dockerfile:
    ```shell
    gcloud builds submit --tag gcr.io/PROJECT-ID/flaskapp
    ```
    Where PROJECT-ID is your GCP project ID. You can get it by running gcloud config get-value project.

2. Upon success, you will see a SUCCESS message containing the image name (gcr.io/PROJECT-ID/flaskapp). The image is stored in Container Registry and can be re-used if desired.

# Deploying to Cloud Run
## To deploy the container image:
1. Deploy using the following command:
    ```shell
    gcloud run deploy --image gcr.io/PROJECT-ID/flaskapp
    ```
    If prompted to enable the API, Reply **y** to enable.

    Replace PROJECT-ID with your GCP project ID. You can view your project ID by running the command ***gcloud config get-value project.***

      * You will be prompted for the service name: press Enter to accept the default name, **flaskapp.**
      * You will be prompted for region: select the region of your choice, for example **us-central1.**
      * You will be prompted to **allow unauthenticated** invocations: respond **y** .
    
    Then wait a few moments until the deployment is complete. On success, the command line displays the service URL.
2. Visit your deployed container by opening the service URL in a web browser.


# Credits
* [Facial Expression Recognition by justinshenk](https://github.com/justinshenk/fer )
* [Cloud Run Documentation: Build and deploy a Python service](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)