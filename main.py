import pickle
import numpy as np 
import lightgbm as lgb
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

model=None
with open('./final_model.pickle', 'rb') as f:
  model = pickle.load(f)

class PredictWert(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        year = json_data['year']
        month = json_data['month']
        prediction = model.predict(np.array([year, month]).reshape(-1, 2))
        return jsonify(prediction = prediction[0])

api.add_resource(PredictWert, '/prediction')

if __name__ == '__main__':
    app.run(debug=True)