
from flask import Flask,jsonify,request
import pandas as pd
import joblib


app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():

    feat_data = request.json

    df = pd.DataFrame([feat_data])

    df = df.reindex(columns=cols)

    prediction = list(model.predict(df))

    return jsonify({'Phone Price ': int(prediction[0])})





if __name__ == "__main__":
    model = joblib.load('PhonePricePredcetionModelV1.pkl')
    cols = joblib.load('Columns.pkl')
    app.run(debug=True,port=5000)
