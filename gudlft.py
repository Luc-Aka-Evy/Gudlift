import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"


competitions = loadCompetitions()
clubs = loadClubs()


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template("500.html"), 500


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    club = [club for club in clubs if club["email"] == request.form["email"]][0]
    return render_template(
        "welcome.html",
        club=club,
        competitions=competitions,
        datetime=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return render_template(
            "booking.html", club=foundClub, competition=foundCompetition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
            datetime=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    if placesRequired > 0 and competition["date"] > str(datetime.now()):
        if int(club["points"]) > (placesRequired * 3):
            competition["numberOfPlaces"] = (
                int(competition["numberOfPlaces"]) - placesRequired
            )
            club["points"] = int(club["points"]) - (placesRequired * 3)
            flash(
                "Great-booking complete! you booked {} places for {}".format(
                    placesRequired, competition["name"]
                )
            )
            return render_template(
                "welcome.html",
                club=club,
                competitions=competitions,
                datetime=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )
        else:
            flash(
                "Something went wrong (maybe you don't have enough points or you try to book more than 12 places or this competitions is already full or over)"
            )
            return render_template(
                "welcome.html",
                club=club,
                competitions=competitions,
                datetime=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )


@app.route("/pointsDisplay")
def pointsDisplay():
    return render_template("points_display_board.html", club=clubs)


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
