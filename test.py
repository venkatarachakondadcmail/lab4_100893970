import boto3
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Replace these with your actual AWS credentials and S3 bucket and key names
aws_access_key_id = 'AKIATWJPBAU4O3LOUPP3'
aws_secret_access_key = 'WdQdQURROu3raA4CsRLvPWysuDTkAcatb4ajxTEH'
bucket_name = 'fishweighttest'
model_key = 'fish_weight_model.pkl'

# Download and load the model on app startup
try:
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    response = s3.get_object(Bucket=bucket_name, Key=model_key)
    model = pickle.loads(response['Body'].read())
except Exception as e:
    print("Error downloading the model:", e)
    model = None


@app.route('/predict', methods=['POST'])
def predict_weight():
    try:
        data = request.get_json()
        length_ver = data['length_ver']
        length_dia = data['length_dia']
        length_cro = data['length_cro']
        height = data['height']
        width = data['width']

        prediction_data = [[length_ver, length_dia, length_cro, height, width]]
        prediction = model.predict(prediction_data)[0]


        return jsonify({'predicted_weight': prediction})

    except Exception as e:
        return jsonify({'error': 'An error occurred during prediction.', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run()
