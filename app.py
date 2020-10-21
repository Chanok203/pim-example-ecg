from flask import Flask, render_template, request
import json
import numpy as np

# LOAD MODEL
# model = ...

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        file = request.files.get("file")
        text = file.stream.read().decode("utf-8")
        lead_2 = np.array(json.loads(text).get("II"))
        print(lead_2.shape)
        # TODO: Something
        # y_pred = model.predict(X)
        # cls = y_pred.argmax()
        # label = cls2label[cls]
        # result = "class = " + label
        return render_template("home.html", result=text)

app.run(debug=True)
