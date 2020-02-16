import os
from os import path
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for

""" special mongo library for flask """
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# To protect our credentials: Load MONGO_URI as environment variable if we run local
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'track_competition'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# Create pymongo instance of app (constructor method)
mongo = PyMongo(app)


@app.route('/')
def main():
    return render_template('main.html',
                           tracks=mongo.db.tracks.find().sort("total_votes", -1),
                           users=mongo.db.users.find())


@app.route('/get_tracks')
def get_tracks():
    return render_template('tracks.html',
                           tracks=mongo.db.tracks.find().sort("total_votes", -1),
                           users=mongo.db.users.find())


@app.route('/add_track')
def add_track():
    return render_template('addtrack.html',
                           users=mongo.db.users.find(),
                           styles=mongo.db.styles.find(),
                           methods=mongo.db.methods.find())


@app.route('/add_user')
def add_user():
    return render_template('adduser.html')


@app.route('/insert_track', methods=['POST'])
def insert_track():
    tracks = mongo.db.tracks
    """ request to get the form, converted to dict """
    track = request.form.to_dict()
    """ Get soundcloud embed code """
    embed_code = track['soundcloud']
    """ strip the track number so we can use our own modified embed code """
    track_position = embed_code.find('track')
    track['soundcloud'] = embed_code[track_position+7:track_position+16]
    """ get the current date and time, and add to the track """
    now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    track.update({'timestamp': now})
    """ insert track in database and return to the track overview page """
    tracks.insert_one(track)
    return redirect(url_for('get_tracks'))


@app.route('/insert_user', methods=['POST'])
def insert_user():
    users = mongo.db.users
    user = request.form.to_dict()
    """ get the current date and time, and add to the user record """
    now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    user.update({'timestamp': now})
    """ insert user in database and return to the track overview page """
    users.insert_one(user)
    return redirect(url_for('get_tracks'))


@app.route('/view_user/<user_id>')
def view_user(user_id):
    return render_template('viewuser.html',
                           user=mongo.db.users.find_one(
                               {"_id": ObjectId(user_id)}))


@app.route('/vote_track/<track_id>')
def vote_track(track_id):
    voted_track = mongo.db.tracks.find_one({"_id": ObjectId(track_id)})
    return render_template('votetrack.html',
                           track=voted_track,
                           users=mongo.db.users.find())


@app.route('/insert_vote/<track_id>', methods=['POST'])
def insert_vote(track_id):
    tracks = mongo.db.tracks
    tracks.update_one({'_id': ObjectId(track_id)},
                      {'$push': {'votes': {
                          'voted_user': request.form.get('user'),
                          'vote': int(request.form.get('vote')),
                          'motivation': request.form.get('motivation')
                      }}})
    """ add the vote to the total for this track """
    tracks.update_one({'_id': ObjectId(track_id)},
                      {'$inc': {'total_votes': int(request.form.get('vote'))}})

    return redirect(url_for('get_tracks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
