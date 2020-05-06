# single_view
a simple django application which reconciles data from file and creats API. And eact.js is used for front-end app.


# Running Instructions
#### For Backend
- create a virtual environment using python3 `python3 -m venv env`
- activate your virtual environment using `source /home/user/env/bin/activate` replace `/home/user/env` with your virtualenv full path.
- install all dependencies using `pip install -r requirements.txt`
- update your db config in `app/app/settings.py` file. Make sure you have installed postgresql.
- migrate your database using `python manage.py migrate`
- run the django app using `python manage.py runserver` 


### For Frontend
- install npm on your local machine globally.
- install yarn using `npm install yarn`
- run `yarn add` or `yarn add package.json` to install all front-end dependencies
- run `yarn start` to start the front-end app