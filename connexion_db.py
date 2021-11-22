from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

import pymysql.cursors

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        #db = g._database = sqlite3.connect(DATABASE)
        db = g._database = pymysql.connect(
            #host="amillet.mysql.pythonanywhere-services.com",
            host="localhost",
            # host="serveurmysql",
            #user="amillet",
            user="votreLogin",
            #passwd="mdpiut9025",
            password="votreMotDePasse",
            # database="amillet$default",
            database="BDD_votreLogin",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return db