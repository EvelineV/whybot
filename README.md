Who does not love MATLAB? And who misses it when they have no longer access to a campus license? Just me? Oh.

## Matlab's favourite easter egg
Type `why` in a Matlab console. Again. And again. Now, you can do the same in Slack with a Slash command. How? 

## How to install
* Fork my repository.
* Customize the responses by adding and removing words to/from the lists in `matlabwhy.py`.
* Deploy the Falcon API. You can do this on [PythonAnywhere](https://www.pythonanywhere.com) using the WSGI file provided, just make sure to change the username and get the filepath right.
* Go to [slack.com/apps/build](slack.com/apps/build), select Make a Custom Integration, and click Slash Commands. Use the command `/why`, have it make a POST request to your app on PythonAnywhere (http://your_username.pythonanywhere.com/why). 
* Install the app (i.e. the Slack App that you built in the previous step) on Slack, give it a profile picture and a good name.
* Type `/why` in one of your conversations.

## Inspiration
This project is just for fun. It is not connected to the actual Matlab product, just inspired by it. Do not take it too seriously, and do not distribute it as if it were actually connected to Matlab. 
