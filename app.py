import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("Home.html")

@flask_app.route("/test")
def test():
    return render_template("About.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]

    # print(float_features)

    prediction = model.predict(features)

    if prediction == 1:
        prediction_text = "Malignant"
    elif prediction == 0:
        prediction_text = "Benign"

    return render_template("About.html", prediction_text = "The cancer is {}".format(prediction_text))

if __name__ == "__main__":
    flask_app.run(debug=True)

