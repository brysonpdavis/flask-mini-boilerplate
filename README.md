# mini-flask-boilerplate
Super simple Flask boilerplate for small web applications, deployable to Heroku. 

### Deploying to Heroku
```sh
$ source venv/bin/activate
(venv) $ heroku login
(venv) $ heroku apps:create myapp
(venv) $ heroku config:set FLASK_APP=myapp.py
(venv) $ heroku local web # Test if your project runs locally!
(venv) $ git push heroku master
```
