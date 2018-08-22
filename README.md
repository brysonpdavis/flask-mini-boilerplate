# mini-flask-boilerplate
Super simple Flask boilerplate for small web applications, deployable to Heroku. 

### Deploying to Heroku
```sh
$ heroku login
$ heroku apps:create myapp
$ heroku config:set FLASK_APP=myapp.py
$ git push heroku master
```
