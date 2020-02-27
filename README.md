# Crowd finding
## Web application to host a music competition
### Milestone project 3 for Code Institute

#### Deployed version:
- [Crowd -Finding](https://crowd-finding.herokuapp.com/)


## Project purpose
The purpose of this application is to host a competition of music tracks for starting musicians. As [soundcloud](https://www.soundcloud.com) is by far the most used hosting website for artists, they can simply use the embed-code provided with each soundcloud track to enter a new track in the contest. Visitors of the website can view the track listing, with some details about the work provided by the artist, and then vote for each track. The more points, the higher the track will appear in the list. After a pre-defined period of time the competition ends and the first five will show on the front page as winners. The host of the competition can then use these tracks to release these as an album on spotify and itunes or media such as cd or vinyl. The host will also get some insight in why certain tracks are liked, and others less, as well as build a database of users to use for a mailing list, to keep them updated on the progress and future actions.    

There is a registration system for users wich divides them into two categories
1. ```Contributors```
2. ```Voters```

The app automatically shows only the features wich the logged in user is allowed to use. People registered as contributors cannot vote, and those registered as voters will not be able to participate in the contest.

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

#### UX

### Mock-ups
The mock-up for this project are in the UXD folder wich you will find in the root of this project.
- [Wireframe](UXD/wireframe.jpg)

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
    - Fonts (Source code pro/Allerta Stencil)
- [Autoprefixer](https://autoprefixer.github.io)
    - CSS prefixes for different browsers 
- [Online-convert](https://image.online-convert.com/convert-to-ico)
    - Convert jpg image to ico for favicon

## Deployment 
This project was deployed on heroku from the ```master branch```

## Deployment instructions
### Follow these instructions to deploy this project:

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

### Local deployment
#### Alternatively you can connect your local folder directy to heroku
- Enter from your local terminal: 
    - ```heroku login```
- Now provide your email and password to connect to heroku
- Enter from the terminal:
    - ```heroku git:remote -a <your chosen app name>```
    - ```git push heroku master```

[Click here to view the deployed website](https://crowd-finding.herokuapp.com/)