from flask import Flask, render_template, make_response, redirect, request, url_for
from flask_bootstrap import Bootstrap
import matplotlib.pyplot as plt
import pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'                           # Ruta donde almacenaremos los archivos cargados 
ALLOWED_EXTENSIONS = {'csv'} # Conjunto de extensiones de archivo permitidas

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route("/")
def index():
    response = make_response(redirect('/upload'))
    return response

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    df = pd.read_csv(file)
    columns = request.form.getlist("columns")
    for column in columns:
        plt.plot(df[column])

    plt.show()

    return render_template("hello.html", columns=columns)