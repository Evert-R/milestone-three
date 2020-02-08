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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
