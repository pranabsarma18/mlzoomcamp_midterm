import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('smoker_prediction')

@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()
    del patient['id']
    # Define the categorical and numerical columns based on your criteria
    categorical = ['hearing(left)', 'hearing(right)', 'dental caries']
    numerical = [col for col in patient.keys() if col not in categorical]
    # Convert specified categorical columns to strings in the test data point
    for col in categorical:
        patient[col] = str(patient[col])

    # Now, 'test_data_point' has undergone the same preprocessing steps as your DataFrame

    X = dv.transform([patient])
    y_pred = model.predict_proba(X)[0,1]
    smoker = y_pred

    result = {
        "smoker_probability": float(y_pred),
        "smoker" : bool(smoker)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)