Awesomebox - your herald of awesomeness
=======================================

Intro
-----
Awesomebox is a little Flask-based Python web app to play theme-song mp3s at the push of a button (bookmarked URL) for
any time it's appropriate to broadcast your awesome skillz to your immediate area.

Dependencies
------------
* [python](http://python.org)
* [pygame](http://pygame.org) - to play theme songs
* [sqlite3](http://sqlite.org) - to store user ids
* [sqlalchemy](http://www.sqlalchemy.org) - to do queries in a cleaner way
* [flask](http://flask.pocoo.com) - to serve up the app

Setup
-----
I've got this app running on a little Dell netbook running Ubuntu 8 connected to some speakers. You have to
start the app as a user in the *audio* group so that sounds can be played on the box. Otherwise, simply grab 
the code, run `python awesome.py` and the app's live. I like to alter my hosts file so that I map the IP address
of the awesomebox to **"awesomebox"**.

Usage
-----
Assuming that the sever is called **awesomebox**, visit:

* [Register as a user](http://awesomebox/register)
   * Add your name
   * Choose a theme song
   * Click *Register!*
* Play your first theme
   * Visit `http://awesomebox/<username>/1` to play your first themesong
* Use your profile to change your themes or add new ones
   * `http://awesomebox/<username>` will take you to your profile page