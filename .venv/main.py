from flask import Flask, render_template, make_response, redirect, request, url_for
from flask_bootstrap import Bootstrap
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route("/")
def index():
    response = make_response(redirect('/upload'))
    return response

@app.route("/upload", methods=["GET","POST"])
def upload():
    df = []
    if request.method == "POST":
        graph_type = request.form["grafico"]

        file = request.files["file"]
        df = pd.read_csv(file)
        columns = request.form.getlist("columns")
        fig = plt.figure()

        if graph_type == "Lineal":
            for column in columns:
                plt.plot(df[column],color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
                plt.title("Linear Grafic")
        elif graph_type == "Barra":
            for column in columns:
                plt.bar(df[column],10,color='red')
                plt.title("Bar Grafic")
        elif graph_type == "Scatter":
           for column in columns:
            #plt.scatter(column[0],column[1],vmin=0, vmax=100)
            plt.scatter(df[column],df[column])
            plt.title("Scatter Grafic")
        elif graph_type == "Pie":
            for column in columns:
                plt.pie(df[column])
                plt.title("Pie Grafic")

        plt.savefig('static/images/my_plot.png')

    return render_template("hello.html", df=df, upload = True, plot="static/images/my_plot.png")

