export PROJECT_ID=zmood-314009
gcloud builds submit --tag gcr.io/$PROJECT_ID/flaskapp_zm:v1
gcloud run deploy flaskapp_zm --image gcr.io/$PROJECT_ID/flaskapp_zm:v1 --region asia-southeast2-a --platform managed
