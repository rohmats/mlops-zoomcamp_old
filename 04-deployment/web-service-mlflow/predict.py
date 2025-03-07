import os
import pickle

import mlflow
from flask import Flask, request, jsonify


# RUN_ID = os.getenv('RUN_ID')
RUN_ID = '3c55362ba332448e95ccf981547f7eaa'

logged_model = f'runs:/{RUN_ID}/model'
# logged_model = 'runs:/aa0767b5c49145e1b52d5cccde7378c3/model'


model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features):
    preds = model.predict(features)
    return float(preds[0])


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
