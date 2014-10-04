Working OpenShift Example
----------------------------

This the repository I pushed to OpenShift and can be used to clone the [original site](http://rcfb-flairgen.rhcloud.com/) in the event of its demise (or for any reason, really). It uses cron to run the updateflairs script in `/.openshift/cron/daily/` which updates the flair values each day. 

How to make it work:

1. [Create a python 2.7 cartridge via the command line](https://developers.openshift.com/en/getting-started-overview.html). Copy everything from here into the folder that was made. Make sure to copy over the files from the static and templates folders in the bottom directory of this repository as well.

2. Add a PostgreSql database to your cartridge and update `/.openshift/cron/daily/updateflairs` and `/wsgi/inlineflairs.py` with the properties of your database. TIP: Use SSH and the commands `printenv OPENSHIFT_POSTGRESQL_DB_HOST`, `printenv OPENSHIFT_POSTGRESQL_DB_PORT`, `printenv OPENSHIFT_DB_USERNAME`, and `printenv OPENSHIFT_DB_PASSWORD` to get these values. The dbname is whatever you named your app. In my case it is `rcfb`.

3. Add cron to your cartridge.

4. Git add/commit and push to OpenShift. 

5. Using SSH, navigate to your cron/daily directory (should be in `app-root/repo/.openshift/cron/daily/`). Run updateflairs with the command `./updateflairs`, adding the flair values to the database for the first time. After this it will update automatically. Alternatively, you could just wait a day for the script to run.

The site should now be available. If not, restart your app. If still not, I'm sorry for putting you through all this.
