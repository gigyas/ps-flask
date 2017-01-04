from __future__ import print_function
import sys

from flask import render_template, url_for, request, redirect, flash
from flask_login import login_required, login_user

from flasky import app, db, login_manager
from forms import BookmarkForm, LoginForm
from models import Bookmark, User

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=Bookmark.newest(5))

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(url=url, description=description, user=logged_in_user())
        db.session.add(bm)
        db.session.commit()
        flash('Stored bookmark: {}'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        _user = User.query.filter_by(username=form.username.data).first()
        sys.stdout.flush()
        if _user is not None:
            login_user(_user, form.remember_me.data)
            flash('Logged in successfuly as {}'.format(_user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('User does not exist')
    return render_template('login.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

