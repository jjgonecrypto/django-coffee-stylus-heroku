django-coffee-stylus-heroku
===========================

starter application to have `django-pipeline` running on heroku, precompiling coffee and stylus assets as needed.


##dependencies

* custom buildpack from [https://github.com/jiaaro/heroku-buildpack-django](https://github.com/jiaaro/heroku-buildpack-django)

* `django-pipeline` for coffee and stylus support


##production (heroku) deploy

1. create the stack on heroku   

        heroku create --stack cedar --buildpack git@github.com:jiaaro/heroku-buildpack-django.git

2. add `/app/bin` to your PATH in Heroku (all node deps including node will be symlinked here) 

        heroku config:add PATH=bin:node_modules/.bin:/usr/local/bin:/usr/bin:/bin:/app/bin


##how it works 

the buildpack enables the `npm_requirements.txt` file where you enter all of your node dependencies.

on heroku push, all npm requirements are added and symlinked under `/app/bin` (eg. `/app/bin/node`, `/app/bin/coffee`, etc)

in `settings_production.py` simply override pipeline settings to point to these symlinks:

    PIPELINE_COFFEE_SCRIPT_BINARY = '/app/bin/coffee'
    PIPELINE_STYLUS_BINARY = '/app/bin/stylus'