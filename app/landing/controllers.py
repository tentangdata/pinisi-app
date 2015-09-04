from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, make_response
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.landing.models import User
from collections import Counter
from random import shuffle
from sqlalchemy import func
import datetime
import re
import StringIO
import random

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

@landing.route("/graph.png")
def simple():
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter

	qty = Counter()
	q = db.session.query(func.date(User.created_at), func.count(User.id)).group_by(func.date(User.created_at))
	for dt in q.all():
		qty[dt[0]] = dt[1]

	fig = Figure()
	ax = fig.add_subplot(111)
	x = []
	y = []
	date = datetime.date(2015, 9, 2) # start date
	delta = datetime.timedelta(days=1)
	while date < datetime.date.today():
		date += delta
		x.append(date)
		y.append(qty[date])
	ax.plot_date(x, y, '-')
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()
	canvas = FigureCanvas(fig)
	png_output = StringIO.StringIO()
	canvas.print_png(png_output)
	response = make_response(png_output.getvalue())
	response.headers['Content-Type'] = 'image/png'
	return response