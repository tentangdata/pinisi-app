from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.landing.models import User
from app.maps.models import Point
from random import shuffle

# Define the blueprint: 'maps', set its url prefix: app.url/maps/
maps = Blueprint('maps', __name__, url_prefix='/maps')

@maps.route('/final/', methods=['GET', 'POST'])
def final():
	if request.method == 'POST':
		if not request.form['level'] or not request.form['lat'] or not request.form['lng']:
			flash('Pastikan Anda sudah memilih satu titik!')
		else:
			point = Point(session['user_id'], request.form['level'], request.form['lat'], request.form['lng'])
			db.session.add(point)
			db.session.commit()
			email = db.session.query(User).filter(User.id == 1).first().email
			points = db.session.query(Point).filter(Point.user_id == session['user_id']).all()
			mandrill.send_email(
		 		from_email='noreply@tentangdata.com',
		 		from_name='Tim Tentang Data',
		 		to=[{'email': email}],
		 		subject='Treasure Hunt',
		 		text='Terima kasih sudah berpartisipasi dalam permainan ini. Berikut adalah titik-titik yang Anda pilih pada setiap lokasi:\n%s' % '\n'.join(points)
		 	)
			return redirect('/success')
	return render_template('maps.html', map=5)

@maps.route('/<level>/', methods=['GET', 'POST'])
def index(level):
	if request.method == 'POST':
		if not request.form['level'] or not request.form['lat'] or not request.form['lng']:
			flash('Pastikan Anda sudah memilih satu titik!')
		else:
			point = Point(session['user_id'], request.form['level'], request.form['lat'], request.form['lng'])
			db.session.add(point)
			db.session.commit()
			if int(level) + 1 != 6:
				return redirect('/maps/%d/' % (int(level) + 1))
			else:
				return redirect('/maps/final/')
	coordinate = session['maps'][int(level) - 1]
	return render_template('maps.html', map=session['maps'][int(level) - 1])