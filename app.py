import pickle

import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/classify',methods=['POST'])
def classify():



    features = request.form.to_dict()
    features = list(features.values())
    features = np.array(features).reshape(1,11)
    res = model.predict(features)
    if res==0:
        t="cette personne ne va pas s'abonner"
    else:
        t="cette personne va s'abonner"

    return render_template('form.html', result=''+t)

if __name__ == "__main__":
    app.run(debug=True)