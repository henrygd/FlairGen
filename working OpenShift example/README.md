Working OpenShift Example
----------------------------

This the repository I pushed to OpenShift and can be used to clone the [original site](http://rcfb-flairgen.rhcloud.com/) in the event of its demise (or for any reason, really). It uses cron to run the updateflairs script in ".openshift/cron/daily/" which updates the flair values each day. This script creates "updatevalue.py" in OpenShift's persistent storage env directory and this is imported by inlineflairs.py. The main app location is in the wsgi folder.

I'll probably add comments soon explaining this better but if I forget you can always contact me for help. Or to remind me how lazy I am.
