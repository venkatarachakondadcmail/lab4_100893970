from flask import Flask, request, jsonify
from flask import render_template
import boto3
import  joblib

app = Flask(__name__)



# # Replace these with your actual AWS credentials and S3 bucket and key names
# aws_access_key_id = 'AKIATWJPBAU4O3LOUPP3'
# aws_secret_access_key = 'WdQdQURROu3raA4CsRLvPWysuDTkAcatb4ajxTEH'
# bucket_name = 'fishweighttest'
# model_key = 'fish_weight_model.pkl'

# # Download and load the model on app startup
# try:
#     import pickle
#     import boto3

#     s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
#     model = pickle.loads(s3.Bucket(bucket_name).Object(model_key).get()['Body'].read())
# except Exception as e:
#     print("Error downloading the model:", e)
#     model = None

model = joblib.load("model.joblib")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_weight():
   
    # Load the traned model
    data = request.get_json()
    length_ver = data['length_ver']
    length_dia = data['length_dia']
    length_cro = data['length_cro']
    height = data['height']
    width = data['width']

    prediction_data = [[length_ver, length_dia, length_cro, height, width]]
    prediction = model.predict(prediction_data)[0]

    return jsonify({'predicted_weight': prediction})

if __name__ == '__main__':
    app.run()

