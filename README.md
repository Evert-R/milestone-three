# Track competition

### Deployed version 
[https://evert-r.github.io/milestone-one](https://evert-r.github.io/milestone-one)




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
- [Photoshop CS6](https://www.adobe.com/products/cs6.html)
    - Image editing 
- [Steinberg Cubase 10](https://new.steinberg.net/cubase/) 
    - Converting music from Wav to Mp3 and FLAC

## Deployment
### Github Pages
This project was deployed via heroku from the ```master branch```

#### This was done following this procedure:
1. Goto the apps page on Heoku: [Heroku](https://dashboard.heroku.com/apps)
2. Click ```New```
3. Select ```Create new app```
4. Enter a unique ```App name```
5. Select your ```Region```
6. Click ```Create App```
7. Go to ```Settings```
8. Click ```Reveal Config Vars```
9. Add the following variables :
    1. IP           -   ```0.0.0.0```
    2. PORT         -   ```5000```
    3. MONGO_URI    -   ```<Your personal MongoDB URI>```

Deploy
click Connect to GitHub
click ok to authorize the connection
use the search button to select the apropiate repository

1. Enter from your local terminal : 
    1. ```heroku login```
            Provide your email and password to connect to heroku
    2. ```heroku git:remote -a <your chosen app name>```
    3. ```git push heroku master```


[Click here to view the deployed website](https://evert-r.github.io/milestone-one)