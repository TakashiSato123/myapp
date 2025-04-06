from flask import request, redirect, url_for, render_template, flash, session
from app_instance import app

@app.route('/')
def home():
    return render_template('index.html')