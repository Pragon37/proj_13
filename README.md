# Proj_13 :Web api Orange lettings County

[Project 13](https://github.com/Pragon37/proj_13)

This project is a refactored API, available as a docker container and deployed on heroku. 

## Installing / Getting started

It is implemented as a DJANGO framework python program. To setup the environment you need to execute the following instructions:

```Windows Powershell
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
To stop and quit the application: CTRL-BREAK.

```
Then you run the web application by loading :
[Project 13] (http://localhost:8000/admin) if you are an administrator
[Project 13] (http://localhost:8000/lettings) to see the available lettings
[Project 13] (http://localhost:8000/profile) if see the customer profile

## Developing


``` Windows Powershell
git clone https://github.com/Pragon37/proj_13
cd proj_13/
```

## Running a docker container
First setup the DJANGO_SECRET_KEY and DJANGO_DEBUG (if needed).

$Env:DJANGO_DEBUG = 0
 0 production mode / 1 debug mode

$Env:DJANGO_SECRET_KEY = 'my_secret_key'

To check that it was successful or to display the current values:

$Env:DJANGO_DEBUG
$Env:DJANGO_SECRET_KEY


After having started Docker Desktop run the following command to execute the most recent release application:

docker run --pull=always -e "PORT=8765" -e DJANGO_DEBUG -e DJANGO_SECRET_KEY -p 8007:8765 pr37docker/proj_13:latest 

or in detached mode

docker run -d  --pull=always -e "PORT=8765" -e DJANGO_DEBUG -e DJANGO_SECRET_KEY -p 8007:8765 pr37docker/proj_13:latest 

Set up you browser with address : 
[oc lettings](http://localhost:8007)
 
Admin login:
-User : admin
-Password: Abc1234!

## Running Heroku
The site is available online at :
[oc-lettings](https://oc-lettings-37.herokuapp.com)

## Creating a new release of the site

-Edit and save the necessary files:

git add .
git commit -m "What was fixed"
git push

This triggers the execution of a circleci pipeline that :
-compiles, lints and tests the new code delivery
-If it is successful it creates and pushes a docker container to docker hub and heroku. The container pushed in
the heroku registry is then deployed.

The heroku registry can be cleaned by deleting and recreating the application:
heroku config
display the current config with the required environment variable

heroku apps:destroy oc-lettings-37
heroku create oc-lettings-37
heroku config:set DJANGO_SECRET_KEY='my_secret_key'

caret (^) and ampersand(&) in  my_secret_key should be enclosed within "".


## Links
- Project homepage : [Project 13](https://github.com/Pragon37/proj_13)
- Repository: https://github.com/Pragon37/proj_13.git

## CI/CD
Consists of 3 jobs:
lint-and-test : to run lint and test on any branches that is pushed to the repository
build-and-push : to build a docker image and push it to docker hub and heroku if there is a new successful push to the git master branch only
deploy-to-heroku : deploy a new container that was pushed to heroku registry

## Testing and monitoring
The API is tested with the following command:

pytest --nomigrations

The API is monitored using the sentry API and the reference incident can be displayed at :
[sentry-debug](https://sentry.io/share/issue/aa90816cdef1487e9ccde3a12d35dc15/)

## Author

Pierre : pragon37@outlook.fr

##Credits
[powershell env variables](https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2)
[deploying django to heroku with docker](https://testdriven.io/blog/deploying-django-to-heroku-with-docker/)
[Very academy : How to Dockerize a django app](https://www.youtube.com/watch?v=W5Ov0H7E_o4)
[very Academy : Sentry Django Integration - Error Reporting](https://www.youtube.com/watch?v=W5Ov0H7E_o4)
[Continuous delivery for free using Docker, CircleCI and Heroku](https://www.codingnagger.com/2018/02/21/continuous-delivery/)
[v2-project-13 discord](https://discord.com/channels/347061157351260161/766332882423250954/859219999625314365)
