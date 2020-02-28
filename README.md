# Crowd finding
## Web application to host a music competition
### Milestone project 3 for Code Institute

#### Deployed version:
- [Crowd -Finding](https://crowd-finding.herokuapp.com/)


## Project purpose
The purpose of this application is to host a competition of music tracks for starting musicians. As [soundcloud](https://www.soundcloud.com) is by far the most used hosting website for artists, they can simply use the embed-code provided with each soundcloud track to enter a new track in the contest. Visitors of the website can view the track listing, with some details about the work provided by the artist, and then vote for each track. The more points, the higher the track will appear in the list. After a pre-defined period of time the competition ends and the highest rated five tracks will show on the front page as winners. The host of the competition can then use these tracks to release these as an album on spotify and itunes or media such as cd or vinyl. The host will also get an insight in why certain tracks are liked, and others less. The app also builds a database of users to be used for a mailing list, to keep them updated on the progress and future actions or advertisements.    

There is a registration system for users wich divides them into two categories
1. ```Contributors```
2. ```Voters```

The app automatically shows only the features wich the logged in user is allowed to use to avoid confusion. People registered as contributors cannot vote, and those registered as voters will not be able to participate in the contest.

A third user role is the ```administrator``` with the following features: 
1. Start a contest
2. End a contest
3. Add or delete creation methods, wich let users select wich equipment or instruments they used
4. Add or delete music styles, to let users select the music style of their track
5. View a user list to use for a mailing list (Users can decide themselves if they want this upon registration)

### Important notices
1. This ia a fictional project for educational purposes created for the [code institute's Full Stack Software Development course](https://codeinstitute.net) and is in no way meant to go online for a broad audience.
2. Authorization was not required for this project and was only implemented to make a distinction between users and wich functions they can use. It in no way will provide the security wich a true authorization system will provide.
3. All user accounts and their information is fictional, passwords are set to ```1234```
4. The tracks already in the database are real. I only used tracks of people that I personally know or made myself. The user accounts of contributers wich added the tracks are again fictional and do not display the actual artists.
5. The admin account can be accessed with the following credentials: ```username: admin``` - ```password: 1234```

## UX
### Mock-up
The mock-up for this project are in the UXD folder wich you will find in the root of this project.
- [Wireframe](UXD/wireframe.jpg)

### Design choices
This app was designed to be used without a learning curve. Only the options that are relevant to the logged in user are shown, so that they will always click the right button. The materialize library was used to provide consistent elements that can be easily used by the user and wich adapt to every screen size. When something does go wrong this is pointed out in the form itself, or if it is database related (password, username or embed-code) the user is redirected back to the form with a message about the mistake. There's also an error page, wich should not appear in 'normal' use. 
Only a few distinctive colors are used so that all elements are clearly seprated and don't blur the overall view.

### User stories
* As a first time visitor I want to see a description of website on my first page load
* As a first time visitor I want to be able to see the tracks that have already been submitted
* As an artist I want to create a user account wich enables me to participate
* As an artist I want to submit my track to the contest
* As an artist I want to see the other entries
* As an artist I want to see the ranking of the tracks
* As a voter I want to create a user account wich enables me to vote 
* As a voter I want to be able to see the tracks that have been submitted
* As a voter I want to vote for a track and leave a motivation
* As a voter I want to have the choice to be updated by email about the contest
* As a voter I want to have the choice to receive emails about future projects
* As the site owner I want to be able to start a new contest
* As the site owner I want to be able to set the end date of the contest
* As the site owner I want to be able to provide a name for the contest
* As the site owner I want to be able to end the contest to see the 5 winners
* As the site owner I want to find new artists to release their music, or to book them for concerts
* As the site owner I want to know why people like or dislike certain tracks
* As the site owner I want to create a database of users for targeted advertisement

### Features
- Main page
  - Provides all the visitors with information about the running or ended contest
- Register
  - Enables all the visitors to register as an active user along with these details:
    -   user name
    -   password
    -   email address
    -   user role
    -   profile pic (Standard will be used when none is provided)
    -   country
    -   city
    -   website (optional)
    -   mailing list subscription (yes/no)   
- Log-in
  - Enables all registered users to log in to their account
- Log-out
  - Enables all users to log-out of their account
- Add a track
  - Enables contributors to add a track to the contest
  - Enables contributors to provide details about the track:
    - Artist name
    - Track title
    - Music style
    - Creation method
    - Free text (description)
    - Credits
    - Creation date
    - License (copyright or Creative Commons)
    - Soundcloud embed code of the track
      - The app will automatically strip the track number from this code to be used in its own embed code wich will provide a general look for all tracks in the list 
- Edit a track (Only available in the track list if the user who submitted the track is also logged in )
    - Enables the user to update the information of the submitted track (except for the soundcloud embed-code)
- View all tracks
  - Enables all users to see a list of the tracks
  - Enables all users to easily see the current rank of the track
  - Enables all users to easily see the total score of the track
  - Enables all users to easily see the music style and creation method of the track
  - Enables all users to listen to all the tracks
  - Enables all users to view the track's details
    - Enables all users to click on the track's user name to see its profile page
  - Enables all users to see the track votes
    - Enables all users to click on the voter's user name to see its profile page
- Profile
  - Enables all users to see other users profiles
  - Enables the loggged in user to update its own details
- Vote (via a track in the list)
  - Enables voters to vote for a track
  - Enables voters to leave a motivation with their vote
- Start contest
  - Enables the administrator to start the contest
  - Enables the administrator to name the contest
  - Enables the administrator to set the start and end date for the contest
- End contest
  - Enables the administrator to end the contest
- Edit styles
  - Enables the administrator to add or delete music styles
- Edit methods
  - Enables the administrator to add or delete creation methods
- User list
  - Enables the administrator to view all registered users
- Mailing list
  -  Enables the administrator to view all subscribers to the mailing list

### Features left to implement
- True secure authentication
- Upload files directly to the server, to be completely independent, played using a local music player
  - for example: [Amplitude.js](https://521dimensions.com/open-source/amplitudejs)
- Upload profile pictures directly to the server to be more user friendly
- Automate the duration of the contest based on the current date 

## Technologies Used
- [VSCode](https://code.visualstudio.com)
    - Code Editor
- [Git bash](https://gitforwindows.org)
    - Version control from windows
- [Heroku]()
    - Deployment
- [Flask](https://palletsprojects.com/p/flask)
    - Python framework
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x)
    - Template handling for flask
- [MongoDB atlas](https://www.mongodb.com)
    - Database cloud service
- [PyMongo](https://github.com/mongodb/mongo-python-driver)
    - Python driver for MongoDB
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest)
    - Bridge between flask and pymongo
- [Materialize](https://materializecss.com)
    - Grid, icons, colapsibles, boilerplate-html
- [Google Fonts](https://fonts.google.com)
    - Fonts (Krona one/Orbitron)
- [Autoprefixer](https://autoprefixer.github.io)
    - CSS prefixes for different browsers 
- [Online-convert](https://image.online-convert.com/convert-to-ico)
    - Convert jpg image to ico for favicon

## Data Structure
### MongoDB
- Database:
    - crowd_finding
#### Collections
##### tracks: 
```{'_id':              ObjectId,   (By mongoDB) 
    'user':             string      (corresponds with users collection)
    'user_id':          ObjectId    (corresponds with users collection)
    'submitted':        string      (date), (DD-MM-YYYY, HH:MM:SS)
    'soundcloud':       string      (stripped from soundcloud embed code)
    'artist_name':      string
    'title':            string
    'style':            string
    'free_text':        string
    'creation_method':  string
    'credits_who':      string
    'credits_what':     string
    'creation_date':    string      (date), (DD-MM-YYYY, HH:MM:SS)
    'license':          string      (file name of license logo)
    'last_updated':     string      (date), (DD-MM-YYYY, HH:MM:SS)
    'total_votes':      int32
    'votes':            array of objects {user: string
                                          user_id: ObjectID
                                          vote: int32
                                          motivation: string}                                
```

##### users: 
```{'_id':              ObjectID,  (by MongoDB) 
    'user_name':        string
    'user_email':       string
    'user_role':        string
    'profile_pic':      string     (URL)
    'user_city':        string
    'user_country':     string
    'user_website':     string     (URL)
    'mailing_list':     string
    'registered':       string     (date), (DD-MM-YYYY, HH:MM:SS)
    'last_updated':     string     (date), (DD-MM-YYYY, HH:MM:SS)
    'password':         string    
```
##### contests: 
```{'_id':              ObjectID,  (by MongoDB) 
    'name':             string
    'start_date':       string     (date), (DD-MM-YYYY)
    'end_date':         string     (date), (DD-MM-YYYY)
    'active':           boolean    (URL)    
```

##### methods: 
```{'_id':              ObjectID,  (by MongoDB) 
    'method':           string    
```
##### styles: 
```{'_id':              ObjectID,  (by MongoDB) 
    'style':           string    
```

## Testing

### Tools
- [w3c Markup Validation](https://validator.w3.org)
    - HTML validation: No errors
- [w3c CSS Validation](https://jigsaw.w3.org/css-validator)
    - CSS validation: No errors
- [Chrome development tools](https://developers.google.com/web/tools/chrome-devtools)
    - Css / responsive behaviour
- [Pep8 online](http://pep8online.com)
    - Python code test 

### Manual testing
#### Not logged in
##### Protection against url's that can be copied from a user that was logged in
- Clicked ```View all tracks```
    - I could only view the tracks
- Entered in the browser ```http://127.0.0.1:5000/add_track```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/view_users```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/start_contest```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/end_contest```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/edit_methods```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/edit_styles```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/mailinglist_users```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/view_user```
    - Redirected to the error page
- Entered in the browser ```http://127.0.0.1:5000/view_user/5e53e9cfa33afb09a25000bb```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/view_track```
    - Redirected to the error page
- Entered in the browser ```http://127.0.0.1:5000/view_track/5e53ea82a33afb09a25000bc```
    - Redirected to the login page with a message to login
- Entered in the browser ```http://127.0.0.1:5000/vote_track```
    - Redirected to the error page
- Entered in the browser ```http://127.0.0.1:5000/vote_track/5e53eb9aa33afb09a25000bf```
    - Redirected to the login page with a message to login

##### Forms
- Menu option: ```Register```
    - clicked ```register``` with no fields filled
      - Got a message to fill out all the fields
    - Filled fields one by one clicking ```register``` each time
      - Got a message to fill out all required fields
    - Filled all required fields but not a valid email address
      - Got the message I should provide a valid email address
    - Filled all required fields but no ```https``` in the website or profile picture url 
      - Got a message to provide a valid url
    - Registered with no profile picture
      - Saw the default picture in my profile
  
- Menu option: ```Log-in```
  - Provided random name
    - Was redirected to the login page with a message that the user is unknown
  - Provided random password
    - Was redirected to the login page with a message that the password is incorrect

#### Logged in as ```contributor```
- Menu option: ```Add a track```
    - clicked ```add your track``` with no fields filled
      - Got a message to fill out all the fields
    - Filled fields one by one clicking ```add your track``` each time
      - Got a message to fill out all required fields
    - Filled all fields but provided a wrong embed code
      - Was redirected to the form with a message the embed code was invalid
    - Entered in the browser ```http://127.0.0.1:5000/vote_track/5e53eb9aa33afb09a25000bf```
      - Was redirected to the error page with the message that a contributor can't vote 

#### Logged in as ```Voter```
- Entered in the browser ```http://127.0.0.1:5000/add_track```
    - Was redirected to the error page with the message that a voter can't participate
- Clicked the ```vote``` button on a track
  - Clicked ```Vote``` with no motivation
    - Got a message to filll out all the fields
  - Clicked ```Vote``` with no track rating
    - Couldn't enter my vote

### Responsive behaviour
#### Screen sizes: 360 - 600 px
- All elements are on a single row
- Container width is maximized
- Mobile menu is used

#### Screen sizes: 600 - 996 px
- Two form elements per row (except for long urls)

#### Screen sizes: 996 - px
- Desktop menu is used

### Issues encountered while testing
- A wrong embed code wasn't detected
  - Implemented a test wich redirects back to the form, providing an error message
  
## Deployment 
This project was deployed on heroku from the ```master branch```

## Deployment instructions
### Follow these instructions to deploy this project:

#### Create the first user (administrator)
- Use the following structure

```{'_id':              ObjectID,  (by MongoDB) 
    'user_name':        STRING     'admin'
    'user_email':       string
    'user_role':        string     'administrator
    'profile_pic':      string     (URL)
    'user_city':        string
    'user_country':     string
    'user_website':     string     (URL)
    'mailing_list':     string
    'registered':       string     (date), (DD-MM-YYYY, HH:MM:SS)
    'last_updated':     string     (date), (DD-MM-YYYY, HH:MM:SS)
    'password':         string    
```

#### Create a new repository
- Create a new folder on your local machine
- Clone the repository to the new local folder:
    - ``` git clone https://github.com/Evert-R/milestone-three ```      
- Rename the remote name:
    - ``` git remote rename origin destination ```
- Check if this was successfull:
    - ``` git remote -v ```
- Assign a new remote:
    - ``` git remote add origin <url of the new repository>```
- Push the local repository to the new remote:
    - ``` git push origin master ```

#### Now first create the heroku app:
- Go to the apps page on Heroku: [Heroku](https://dashboard.heroku.com/apps)
- Click ```New```
- Select ```Create new app```
- Enter a unique ```App name```
- Select your ```Region```
- Click ```Create App```
- Go to ```Settings```
- Click ```Reveal Config Vars```
- Add the following variables :
    1. IP           -   ```0.0.0.0```
    2. PORT         -   ```5000```
    3. MONGO_URI    -   ```<Your personal MongoDB URI>```
    4. secret_key   -   ```<secret code to enable sessions in flask>```

#### Finally connect heroku to the github repository
- In heroku click ``` Connect to GitHub ```
- click ```Ok``` to authorize the connection
- use the search button to select the apropiate repository

#### Alternatively you can connect your local folder directy to heroku
- Enter from your local terminal: 
    - ```heroku login```
- Now provide your email and password to connect to heroku
- Enter from the terminal:
    - ```heroku git:remote -a <your chosen app name>```
    - ```git push heroku master```

#### Local deployment
- First in the root folder create a new file named: ```env.py```
    - Put the following code in the file:

          import os
          os.environ["MONGO_URI"] = "<Your personal MongoDB URI>"
          os.environ["secret_key"] = "<randum_string>"

    - The app will first look for this file to load the environment variables
    - If this file is not found it assumes that they are allready present in the environment (For example heroku)
    - This is to ensure our credentials are not exposed on github (add this file to the ```.gitignore``` file)

- To create a virtual environment enter from the terminal in you IDE: 
    - ```python -m .venv venv```
- Now activate the virtual envirenment
    - ```.venv\Scripts\activate```
- Install the requirements
    - ```pip -r requirements.txt```
- Start the app
    - ```python -m flask run```

## Credits
### Media content
- Default profile picture & copyright sign
  - [Pixabay](https://pixabay.com)
- Creative commons logos
  - [Creative Commons](https://creativecommons.org)

[Click here to view the deployed website](https://crowd-finding.herokuapp.com)