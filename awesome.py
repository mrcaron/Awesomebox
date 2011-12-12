from __future__ import with_statement
from flask import Flask, render_template, request, redirect, url_for
import subprocess
from database import db_session, init_db
from models import User
import os.path
import os
import shutil
import eyeD3
import pygame
import pygame.mixer
from pygame.locals import *
import glob

#import sqlite3

THEME_SONGS = 'static/theme_songs'
ALLOWED_EXTENSIONS = set(['mp3'])
MUSIC_END = USEREVENT + 1

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = THEME_SONGS

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def home():	
	return render_template("home.html")

@app.route("/init")
def init():
	init_db()
	return "Initialized!"

@app.route("/<username>")
def profile(username):
	u = User.query.filter(User.uid == username).first()
	if u:
		mp3s = sorted(glob.glob("%s/%s_theme_*" % (app.config['UPLOAD_FOLDER'],username)))
		#mp3fname = os.path.join(app.config['UPLOAD_FOLDER'], u.mp3)
		mp3list = []
		for f in mp3s:
			tag = eyeD3.Tag()
			tag.link(f)
			mp3list.append([f, tag.getTitle()])
		return render_template("profile.html", uid=u.uid, mp3s=mp3list)
	return "%s is not an awesome user"

@app.route("/<username>/<themeId>")
def awesome(username,themeId):
	# lookup sound for username
	usr = User.query.filter(User.uid == username).first()
	if usr is None:
		return "%s isn't registered to be AWESOME. :(" % username
	
	mp3fname = os.path.join(app.config['UPLOAD_FOLDER'], "%s_theme_%s.mp3" % (username,themeId))
	tag = eyeD3.Tag()
	tag.link(mp3fname)

	#print "calling mikehup mpg123 %s from %s &" % (mp3fname,os.getcwd());
	#subprocess.call('mpg123 %s' % mp3fname, shell=True)
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.queue(mp3fname)
	else:
		pygame.mixer.music.load(mp3fname)
		pygame.mixer.music.play()
		pygame.mixer.music.set_endevent(MUSIC_END)
	return render_template('awesome.html', title=tag.getTitle(), uid=username)

@app.route("/register")
@app.route("/register/<uid>")
def register_user(uid=None):
	return render_template('register.html', uid=uid)

@app.route("/add", methods=['POST'])
def add():
	f = request.files['mp3']
	if f and allowed_file(f.filename):
		u = User(request.form['uid'], "%s_theme.mp3" % request.form['uid'])
		fname = os.path.join(app.config['UPLOAD_FOLDER'], u.mp3)
		f.save(fname)
		if (os.path.exists(fname)):
			db_session.add(u)
			db_session.commit()
			return redirect("/%s" % u.uid)
		return "Error saving file"
	return "Error reading file"

@app.route("/change", methods=['POST'])
def change():
	u = User.query.filter(User.uid == request.form['uid']).first()

	if u:
		for f in request.files.items():
			fname = ""
			print "File: ",f[0]
			if f[0].startswith("new_theme"):
				mp3s = glob.glob("%s/%s_theme_*" % (app.config['UPLOAD_FOLDER'],u.uid))
				fname = "%s_theme_%i.mp3" % (u.uid, len(mp3s)+1)
			else: 
				fname = "%s_%s.mp3" % (u.uid,f[0])

			if f[1] and allowed_file(f[1].filename):
				new_fname = "new_%s" % fname
				fname = os.path.join(app.config['UPLOAD_FOLDER'], fname)
				new_fname = os.path.join(app.config['UPLOAD_FOLDER'], new_fname)

				if os.path.exists(new_fname): 
					os.remove(new_fname)
				f[1].save(new_fname)
				if os.path.exists(new_fname):
					shutil.copyfile(new_fname, fname)
					os.remove(new_fname)
					return redirect("/%s" % u.uid)
				return "You no awesome. Try a file that works!"
		return "%s isn't awesome. <a href=\"/register\">Reigster first</a>"

@app.route("/unregister/<username>")
def unregister(username):
	u = User.query.filter(User.uid == username).first()
	if u:
		os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], u.mp3))
		db_session.delete(u)
		db_session.commit()
		return "unregistered %s" % username
	return "%s doesn't exist." % username

@app.teardown_request
def shutdown_session(exception=None):
	db_session.remove()


if __name__ == "__main__":
	pygame.mixer.init(22050,-16,2,2048)
	app.run(host='0.0.0.0', port=80)
	pygame.mixer.quit()
