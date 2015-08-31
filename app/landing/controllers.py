from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.landing.models import User
from random import shuffle
import re

# Define the blueprint: 'index', set its url prefix: app.url/
landing = Blueprint('index', __name__)

@landing.route('/', methods=['GET'])
def hello():
	return render_template('index.html')

@landing.route('/cara-main', methods=['GET'])
def how_to_play():
	return render_template('cara-main.html')

@landing.route('/perompak', methods=['GET'])
def clue():
	return render_template('perompak.html')

@landing.route('/aturan-main', methods=['GET', 'POST'])
def rules():
	if request.method == 'POST':
		if not request.form['email']:
			flash('Apakah Anda sudah memasukkan email dengan benar?')
		else:
			EMAIL_REGEX = re.compile('^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$')
			try:
				if not EMAIL_REGEX.match(request.form['email']):
					raise ValueError("E-mail yang Anda daftarkan tidak valid!")
				user = User(request.form['email'], request.headers.get('User-Agent'))
				db.session.add(user)
				db.session.commit()
				session['user_id'] = user.id
				session['maps'] = range(5)
				shuffle(session['maps'])
				return redirect('/perompak')
			except ValueError, e:
				flash(e)
			except Exception, e:
				flash("Ada masalah saat mendaftarkan e-mail Anda.")
	return render_template('aturan-main.html')

@landing.route('/success', methods=['GET'])
def success():
	treasures = ', '.join(['keris, sasando, dan koin emas'])
	session.clear()
	return render_template('end.html', treasures=treasures)

@landing.route('/tentang-pinisi', methods=['GET'])
def about():
	return render_template('about.html')