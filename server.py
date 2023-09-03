from flask import Flask, render_template
import datetime as dt
import requests


app = Flask(__name__)


@app.route('/')
def first_page():
    year = dt.datetime.now().year
    return render_template("index.html", year=year)


@app.route('/guess/<name>')
def guess_page(name):
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template("guess.html", name=name.capitalize(), age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
