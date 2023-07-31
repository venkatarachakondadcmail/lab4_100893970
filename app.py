from flask import Flask, request, jsonify
import joblib
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_weight():

   
    model = joblib.load('fish_weight_model.pkl')
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

