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
        review = request.get_json()
        data = [review['review']]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect).tolist()
        return jsonify({'isItOk': json.dumps(my_prediction)})


if __name__ == '__main__':
    app.run(debug=True)
