import os
from os import path
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session

""" special mongo library for flask """
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

""" To protect our credentials: Load MONGO_URI and secret_key as environment variables if we run local """
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'track_competition'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

""" Get secret key to enable sessions """
app.secret_key = os.getenv('secret_key')

# Create pymongo instance of app (constructor method)
mongo = PyMongo(app)


@app.route('/')
def main():
    current_contest = mongo.db.users.find_one(
        {'user_name': 'administrator'})
    session['start_date'] = current_contest['start_date']
    session['end_date'] = current_contest['end_date']
    return render_template('main.html',
                           tracks=mongo.db.tracks.find().sort("total_votes", -1),
                           )


@app.route('/login')
def login():
    return render_template('login.html',
                           users=mongo.db.users.find().sort('user_name'))


@app.route('/activate_user', methods=['POST'])
def activate_user():
    user = request.form.get('user').split(',')
    session['user_id'] = user[0]
    session['user_name'] = user[1]
    return redirect(url_for('get_tracks'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('get_tracks'))


@app.route('/start_contest')
def start_contest():
    return render_template('startcontest.html')


@app.route('/insert_contest', methods=['POST'])
def insert_contest():
    users = mongo.db.users
    users.update_one({'user_name': 'administrator'},
                     {'$set': {
                         'start_date': request.form.get('start_date'),
                         'end_date': request.form.get('end_date')
                     }})
    return redirect(url_for('get_tracks'))


@app.route('/get_tracks')
def get_tracks():
    if mongo.db.tracks.count_documents({}) == 0:
        return render_template('tracks.html',
                               no_tracks=True)
    else:
        return render_template('tracks.html',
                               tracks=mongo.db.tracks.find().sort("total_votes", -1),
                               users=mongo.db.users.find().sort('user_name'),
                               styles=mongo.db.styles.find().sort('style'),
                               methods=mongo.db.methods.find().sort('method'))


@app.route('/get_tracks_filtered', methods=['POST'])
def get_tracks_filtered():
    if request.form.get('style'):
        filter_by = {"style": request.form.get('style')}
    if request.form.get('creation_method'):
        filter_by = {"creation_method": request.form.get('creation_method')}
    return render_template('tracks.html',
                           tracks=mongo.db.tracks.find(
                               filter_by).sort("total_votes", -1),
                           users=mongo.db.users.find().sort('user_name'),
                           styles=mongo.db.styles.find().sort('style'),
                           methods=mongo.db.methods.find().sort('method'))


@app.route('/add_track')
def add_track():
    return render_template('addtrack.html',
                           users=mongo.db.users.find(),
                           styles=mongo.db.styles.find().sort('style'),
                           methods=mongo.db.methods.find().sort('method'))


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
    track.update(
        {'user': session['user_name'], 'user_id': session['user_id'], 'submitted': now})
    """ insert track in database and return to the track overview page """
    tracks.insert_one(track)
    return redirect(url_for('get_tracks'))


@app.route('/view_track/<track_id>')
def view_track(track_id):
    return render_template('viewtrack.html',
                           track=mongo.db.tracks.find_one(
                               {"_id": ObjectId(track_id)}),
                           users=mongo.db.users.find().sort('user_name'),
                           styles=mongo.db.styles.find().sort('style'),
                           methods=mongo.db.methods.find().sort('method'))


@app.route('/update_track/<track_id>', methods=['POST'])
def update_track(track_id):
    tracks = mongo.db.tracks
    """ get the current date and time, and add to the user record """
    now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    """ insert user in database and return to the track overview page """
    tracks.update({"_id": ObjectId(track_id)},
                  {'$set':
                   {'artist_name': request.form.get('artist_name'),
                    'title': request.form.get('title'),
                    'style': request.form.get('style'),
                    'free_text': request.form.get('free_text'),
                    'creation_method': request.form.get('creation_method'),
                    'credits_who': request.form.get('credits_who'),
                    'credits_what': request.form.get('credits_what'),
                    'creation_date': request.form.get('creation_date'),
                    'license': request.form.get('license'),
                    'last_updated': now
                    }})
    return redirect(url_for('get_tracks'))


@app.route('/add_user')
def add_user():
    return render_template('adduser.html')


@app.route('/insert_user', methods=['POST'])
def insert_user():
    users = mongo.db.users
    user = request.form.to_dict()
    """ get the current date and time, and add to the user record """
    now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    user.update({'registered': now, 'last_updated': now})
    """ insert user in database and return to the track overview page """
    users.insert_one(user)
    return redirect(url_for('login'))


@app.route('/view_user/<user_id>')
def view_user(user_id):
    return render_template('viewuser.html',
                           user=mongo.db.users.find_one(
                               {"_id": ObjectId(user_id)}))


@app.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    users = mongo.db.users
    """ get the current date and time, and add to the user record """
    now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    """ insert user in database and return to the track overview page """
    users.update({"_id": ObjectId(user_id)},
                 {'$set':
                  {'user_name': request.form.get('user_name'),
                   'user_email': request.form.get('user_email'),
                   'profile_pic': request.form.get('profile_pic'),
                   'user_city': request.form.get('user_city'),
                   'user_country': request.form.get('user_country'),
                   'user_website': request.form.get('user_website'),
                   'mailing_list': request.form.get('mailing_list'),
                   'last_updated': now
                   }})
    return redirect(url_for('get_tracks'))


@app.route('/vote_track/<track_id>')
def vote_track(track_id):
    voted_track = mongo.db.tracks.find_one({"_id": ObjectId(track_id)})
    return render_template('votetrack.html',
                           track=voted_track)


@app.route('/insert_vote/<track_id>', methods=['POST'])
def insert_vote(track_id):
    tracks = mongo.db.tracks
    tracks.update_one({'_id': ObjectId(track_id)},
                      {'$push': {'votes': {
                          'user': session['user_name'],
                          'user_id': session['user_id'],
                          'vote': int(request.form.get('vote')),
                          'motivation': request.form.get('motivation')
                      }}})
    """ add the vote to the total for this track """
    tracks.update_one({'_id': ObjectId(track_id)},
                      {'$inc': {'total_votes': int(request.form.get('vote'))}})

    return redirect(url_for('get_tracks'))


@app.route('/edit_methods')
def edit_methods():
    return render_template('editmethods.html',
                           methods=mongo.db.methods.find().sort('method'))


@app.route('/insert_method', methods=['POST'])
def insert_method():
    method = request.form.to_dict()
    methods = mongo.db.methods
    methods.insert_one(method)
    return redirect(url_for('edit_methods'))


@app.route('/delete_method/<method_id>')
def delete_method(method_id):
    methods = mongo.db.methods
    methods.delete_one({'_id': ObjectId(method_id)})
    return redirect(url_for('edit_methods'))


@app.route('/edit_styles')
def edit_styles():
    return render_template('editstyles.html',
                           styles=mongo.db.styles.find().sort('style'))


@app.route('/insert_style', methods=['POST'])
def insert_style():
    style = request.form.to_dict()
    styles = mongo.db.styles
    styles.insert_one(style)
    return redirect(url_for('edit_styles'))


@app.route('/delete_style/<style_id>')
def delete_style(style_id):
    styles = mongo.db.styles
    styles.delete_one({'_id': ObjectId(style_id)})
    return redirect(url_for('edit_styles'))


@app.route('/reset_contest')
def reset_contest():
    tracks = mongo.db.tracks
    """tracks.drop()"""
    return redirect(url_for('get_tracks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
