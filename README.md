Awesomebox - your herald of awesomeness
=======================================

Intro
-----
Awesomebox is a little Flask-based Python web app to play theme-song mp3s at the push of a button (bookmarked URL) for
any time it's appropriate to broadcast your awesome skillz to your immediate area. This is just a little thing I whipped
up for fun while working, it's not robust, it's not altogether "finished" (i.e. there's more I want to add to it and
error checking is lacking). But feel free to fork it and rock out some improvements. Please share your improvements
via pull requests!

Dependencies
------------
* [python](http://python.org)
* [pygame](http://pygame.org) - to play theme songs
* [sqlite3](http://sqlite.org) - to store user ids
* [sqlalchemy](http://www.sqlalchemy.org) - to do queries in a cleaner way
* [flask](http://flask.pocoo.org) - to serve up the app
* [eyeD3](http://eyed3.nicfit.net/) - to handle mp3 metadata

Setup
-----
I've got this app running on a little Dell netbook running Ubuntu 8 connected to some speakers. You have to
start the app as a user in the *audio* group so that sounds can be played on the box. Otherwise, simply grab 
the code, run `python awesome.py` and the app's live. I like to alter my hosts file so that I map the IP address
of the awesomebox to **"awesomebox"**.

Usage
-----
Assuming that the sever is called **awesomebox**:

* Visit `http://awesomebox/init` to initialize the database
* Visit `http://awesomebox/register` to register as a user
   * Add your name
   * Choose a theme song
   * Click *Register!*
* Play your first theme
   * Visit `http://awesomebox/<username>/1` to play your first themesong
* Use your profile to change your themes or add new ones
   * `http://awesomebox/<username>` will take you to your profile page

[![endorse](http://api.coderwall.com/mrcaron/endorsecount.png)](http://coderwall.com/mrcaron)
