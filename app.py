from flask import Flask
from flask import render_template
from flask import url_for
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello_world():
    x = np.linspace(.0,1.0,100)
    y = np.sin(x)

        
    # print(url_for('dist', filename='style.css'))

    return render_template("index.html")