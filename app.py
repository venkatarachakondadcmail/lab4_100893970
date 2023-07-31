from flask import Flask, request, jsonify
from flask import render_template
import boto3
import  joblib

app = Flask(__name__)


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

