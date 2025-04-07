from flask import request, redirect, url_for, render_template, flash, session
from app_instance import app, db
from functools import wraps
from models.texts import Text

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

# @app.route('/')
# @login_required
# def index():
    # return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        text = Text(request.form['text'])
        db.session.add(text)
        db.session.commit()
        return redirect(url_for('index'))
    
    texts = Text.query.order_by(Text.id.desc()).all()
    return render_template('index.html', texts=texts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('index'))

@app.errorhandler(404)
def non_existent_route(error):
    return redirect(url_for('login'))

