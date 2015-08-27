from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.landing.models import User
from random import shuffle

# Define the blueprint: 'index', set its url prefix: app.url/
landing = Blueprint('index', __name__)

@landing.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		if not request.form['email']:
			flash('Apakah Anda sudah memasukkan email dengan benar?')
		else:
			try:
				user = User(request.form['email'], request.headers.get('User-Agent'))
				db.session.add(user)
				db.session.commit()
				session['user_id'] = user.id
				session['maps'] = range(5)
				shuffle(session['maps'])
				return redirect('/maps/1/')
			except Exception, e:
				flash("Ada masalah saat mendaftarkan e-mail Anda.")
	return render_template('index.html')

@landing.route('/success', methods=['GET'])
def success():
	treasures = request.args.get('item')
	return render_template('success.html', treasures=treasures)