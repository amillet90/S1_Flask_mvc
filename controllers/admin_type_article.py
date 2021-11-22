#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

admin_type_article = Blueprint('admin_type_article', __name__,
                        template_folder='templates')

@admin_type_article.route('/type-article/show')
def show_type_article():
    mycursor = get_db().cursor()
    sql = "SELECT * FROM type_article"
    mycursor.execute(sql)
    types_articles = mycursor.fetchall()
    return render_template('type_article/show_type_article.html', types_articles=types_articles)

@admin_type_article.route('/type-article/add', methods=['GET'])
def add_type_article():
    return render_template('type_article/add_type_article.html')

@admin_type_article.route('/type-article/add', methods=['POST'])
def valid_add_type_article():
    libelle = request.form.get('libelle', '')
    tuple_insert = (libelle,)
    mycursor = get_db().cursor()
    sql = "INSERT INTO type_article(libelle) VALUES (%s);"
    mycursor.execute(sql, tuple_insert)
    get_db().commit()
    message = u'type ajouté , libellé :'+libelle
    flash(message)
    return redirect(url_for('admin_type_article.show_type_article'))

@admin_type_article.route('/type-article/delete', methods=['POST'])
def delete_type_article():
    #id_type_article = request.args.get('id', '')
    id_type_article = request.form.get('id', '')
    mycursor = get_db().cursor()
    tuple_delete = (id_type_article,)
    sql = "DELETE FROM type_article WHERE id = %s;"
    mycursor.execute(sql, tuple_delete)
    get_db().commit()
    flash(u'un type d\'article supprimé, id : ' + id_type_article)
    return redirect(url_for('admin_type_article.show_type_article'))

@admin_type_article.route('/type-article/edit/<int:id>', methods=['GET'])
def edit_type_article(id):
    mycursor = get_db().cursor()
    sql = "SELECT id,libelle FROM type_article where id=%s"
    mycursor.execute(sql, (id,))
    type_article = mycursor.fetchone()
    return render_template('type_article/edit_type_article.html', type_article=type_article)

@admin_type_article.route('/type-article/edit', methods=['POST'])
def valid_edit_type_article():
    libelle = request.form['libelle']
    id_type_article = request.form.get('id', '')
    tuple_update = (libelle, id_type_article)
    mycursor = get_db().cursor()
    sql = "UPDATE type_article SET libelle =%s WHERE id = %s;"
    mycursor.execute(sql, tuple_update)
    get_db().commit()
    flash(u'type article modifié, id: ' + id_type_article + " libelle : " + libelle)
    return redirect(url_for('admin_type_article.show_type_article'))
