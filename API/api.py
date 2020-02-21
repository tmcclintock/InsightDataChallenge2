"""
Small flask API to query a trained logistic regression classifier
for breast cancer detection.
"""
import pickle
from sklearn.linear_model import LogisticRegression
from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

#Get the arguments
parser = reqparse.RequestParser()
parser.add_argument('data')

model_dir = r"./trained_logistic_regressor.pkl"

class BCCPredictor(Resource):
    def get(self):
        args = parser.parse_args()
        user_query = args['data']

        data = user_query.split(',')
        data = [float(i) for i in data]

        model = pickle.load(open(model_dir, 'rb'))
        prediction = model.predict([data])
        
        # create JSON object
        if prediction[0] == 1:
            return {'prediction': 'Malignant'}
        else:
            return {'prediction': 'Benign'}

api.add_resource(BCCPredictor, '/')

if __name__ == '__main__':
    app.run(port=7000, debug=True)
