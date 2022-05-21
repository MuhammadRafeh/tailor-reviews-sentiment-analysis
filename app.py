# Importing essential libraries
from flask import Flask, render_template, request, jsonify
import pickle

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'voting_clf.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('countvector.pkl', 'rb'))

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        review = request.form['review']
        data = [review]
        if type(review) == 'list':
            data = review
        vect = cv.transform(data).toarray()
        prediction = classifier.predict(vect)
        return jsonify({"isItGood": prediction})


if __name__ == '__main__':
    app.run(debug=True)
