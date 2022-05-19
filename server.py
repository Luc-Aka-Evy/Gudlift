import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions

app = Flask(__name__)
app.secret_key = 'something_special'


competitions = loadCompetitions()
clubs = loadClubs()


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary',methods=['POST'])
def showSummary():
    date = "2020-04-27 10:00:00"
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions, datetime=date)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    date = "2020-04-27 10:00:00"
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions, datetime=date)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    date = "2020-04-27 10:00:00"
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired <= int(club['points']):
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        club['points'] = int(club['points'])-placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions, datetime=date)
    else:
        flash("Something went wrong (maybe you don't have enough points or you try to book more than 12 places)")
        return render_template('welcome.html', club=club, competitions=competitions, datetime=date)


@app.route('/pointsDisplay')
def pointsDisplay():
    return render_template('points_display_board.html', club=clubs)

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))