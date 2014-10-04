Working Heroku Example
----------------------------

This a repository I tested with Heroku and can be used to clone the [original site](http://rcfb-flairgen.rhcloud.com/) in the event of its demise (or for any reason, really). It uses the Heroku scheduler to run updateflairs.py, which updates the flair values each day. 

How to make it work:

1. [Get started with Heroku and create an app](https://devcenter.heroku.com/articles/getting-started-with-python). Copy everything from here into the folder you will be using (delete anything else in it besides the hidden .git folder). Make sure to copy over the files from the static and templates folders in the bottom directory of this repository.

2. Make a PostgreSql database through Heroku and update `updateflairs.py` and `inlineflairs.py` with the properties of your database. 

4. Git add/commit and push to Heroku. 

5. Run updateflairs.py with the command `heroku run python updateflairs.py` adding the flair values to the database for the first time.

6. Restart your app with the command `heroku restart`. The site should now be operational!

7. Lastly, add the [Heroku scheduler add-on](https://addons.heroku.com/scheduler) to your app and set it to run `python updateflairs.py` every 24 hours. The flair values will now be updated automatically!
