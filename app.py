# Importing necessary libraries
from flask import Flask, request, jsonify
import pickle
import json

# Loading Multinomial Naive Bayes model and CountVectorizer object
filename = 'voting_clf.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('countvector.pkl', 'rb'))

app = Flask(__name__)


@app.route('/', methods=['POST'])
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
    app.run(debug=True)
