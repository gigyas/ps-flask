from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

from forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xe2\x0c\xed\x96\x15\xe9\xc6\x0f\xcf\x1f\xd5\xc3\xfa\xaf\xac\x91~?4n\xde\xbc\xe2\\'

bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user='matt',
        date=datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url)
        flash('Stored bookmark: {}'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)