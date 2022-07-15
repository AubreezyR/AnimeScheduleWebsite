import pandas as pd
from jikanpy import Jikan
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=['POST'])
def animeSchedule():
    jikan = Jikan()

    dayOfWeek = request.form["text"]

    listOfAnimeData = jikan.schedule(dayOfWeek)[dayOfWeek]
    animeForDay = {}

    for items in listOfAnimeData:
        genres = []
        for genre in items['genres']:
            genres.append(genre['name'])

        animeForDay[items['title']] = genres
    aS = str(animeForDay).replace(":", "").replace("[", ", Genre : ").strip("{}.").replace("'", "").replace("],"," | ").replace("]", "")

    return render_template('form.html', s=aS, d=dayOfWeek)


# def getDay(FlaskForm):
#     day = StringField("Day of The Week", validators=[DataRequired()])
#     submit = SubmitField("Get schedule")


# add in a route for my function app.route()
@app.route("/")
def home():
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)


