import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/test")
def test():
    return render_template("About.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]

    # print(float_features)

    prediction = model.predict(features)

    if prediction == 1:
        prediction_text = "Malignant"
    elif prediction == 0:
        prediction_text = "Benign"

    return render_template("About.html", prediction_text = "The Tumor is {}".format(prediction_text))

if __name__ == "__main__":
    app.run(debug=True, port="2908")

