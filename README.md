# Tailor Reviews Sentiment Analysis
A Flask based web api where anyone can check it's reviews related tailor/clothes if it is good or bad one, 1 for good and 0 for bad review.

## Usage
```js
const data = { review: ['this is a bad cloth', 'nice one'] };
getData = async () => {
    await fetch('https://tailors-nlp.herokuapp.com/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
            console.log(data);
    })
}
```
