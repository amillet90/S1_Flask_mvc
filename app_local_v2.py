#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g
from flask import Blueprint
#pip install flask_wtf
# from flask_wtf.csrf import CSRFProtect
# from flask_wtf.csrf import CSRFError

from controllers.admin_article import *
from controllers.admin_type_article import *

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'
#
# csrf = CSRFProtect()
# csrf.init_app(app)

# @app.errorhandler(CSRFError)
# def handle_csrf_error(e):
#     return render_template('csrf_error.html', reason=e.description), 400

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def show_accueil():
    return render_template('layout.html')

app.register_blueprint(admin_article)
app.register_blueprint(admin_type_article)

if __name__ == '__main__':
    app.run()

