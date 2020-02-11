import os
from os import path
from flask import Flask, render_template, redirect, request, url_for

# special mongo library for flask
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
def get_tracks():
    return render_template('tracks.html',
                           tracks=mongo.db.tracks.find(),
                           users=mongo.db.users.find())


@app.route('/add_track')
def add_track():
    return render_template('addtrack.html',
                           users=mongo.db.users.find(),
                           styles=mongo.db.styles.find(),
                           methods=mongo.db.methods.find())


@app.route('/insert_track', methods=['POST'])
def insert_track():
    tracks = mongo.db.tracks
    # request to get the form, converted to dict
    track = request.form.to_dict()
    embed_code = track['soundcloud']
    track_position = embed_code.find('track')
    track['soundcloud'] = embed_code[track_position+7:track_position+16]
    tracks.insert_one(track)
    return redirect(url_for('get_tracks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
