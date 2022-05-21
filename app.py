# Importing necessary libraries
from flask import Flask, request, jsonify
import pickle
import json
from flask_cors import CORS, cross_origin

# Loading Multinomial Naive Bayes model and CountVectorizer object
filename = 'voting_clf.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('countvector.pkl', 'rb'))

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/', methods=['POST'])
@cross_origin()
def home():
    if request.method == 'POST':
        jsonData = request.get_json()
        data = [jsonData['review']]
        if type(jsonData['review']) is list:
            data = jsonData['review']
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect).tolist()
        return jsonify({'isItGood': json.dumps(my_prediction)})


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
