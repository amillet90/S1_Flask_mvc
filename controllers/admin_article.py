#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

admin_article = Blueprint('admin_article', __name__,
                        template_folder='templates')

@admin_article.route('/article/show')
def show_article():
    mycursor = get_db().cursor()
    sql = "SELECT * FROM article"
    mycursor.execute(sql)
    articles = mycursor.fetchall()
    # print(articles)
    return render_template('article/show_article.html', articles=articles)

@admin_article.route('/article/add', methods=['GET'])
def add_article():
    mycursor = get_db().cursor()
    sql = "SELECT * FROM type_article"
    mycursor.execute(sql)
    types_articles = mycursor.fetchall()
    return render_template('article/add_article.html', types_articles=types_articles)

@admin_article.route('/article/add', methods=['POST'])
def valid_add_article():
    nom = request.form.get('nom', '')
    type_article_id = request.form.get('type_article_id', '')
   # type_article_id = int(type_article_id)
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')
    tuple_insert = (nom,type_article_id,prix,stock,description,image)
    sql = "INSERT INTO article(nom,type_article_id,prix,stock,description,image) VALUES (%s,%s,%s,%s,%s,%s);"
    mycursor = get_db().cursor()
    mycursor.execute(sql, tuple_insert)
    get_db().commit()
    print(u'article ajouté , nom: ', nom, ' - type_article:', type_article_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'article ajouté , nom:'+nom + '- type_article:' + type_article_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message)
    return redirect(url_for('admin_article.show_article'))

@admin_article.route('/article/delete', methods=['POST'])
def delete_article():
    # id = request.args.get('id', '')
    id = request.form.get('id', '')
    tuple_delete = (id,)
    sql = "DELETE FROM article WHERE id = %s;"
    mycursor = get_db().cursor()
    mycursor.execute(sql, tuple_delete)
    get_db().commit()
    print("un article supprimé, id :", id)
    flash(u'un article supprimé, id : ' + id)
    return redirect(url_for('admin_article.show_article'))

@admin_article.route('/article/edit/<int:id>', methods=['GET'])
def edit_article(id):
    mycursor = get_db().cursor()
    sql = "SELECT * FROM article where id=%s"
    mycursor.execute(sql, (id,))
    article = mycursor.fetchone()
    sql = "SELECT * FROM type_article"
    mycursor.execute(sql)
    types_articles = mycursor.fetchall()
    return render_template('article/edit_article.html', article=article, types_articles=types_articles)

@admin_article.route('/article/edit', methods=['POST'])
def valid_edit_article():
    nom = request.form['nom']
    id = request.form.get('id', '')
    type_article_id = request.form.get('type_article_id', '')
    #type_article_id = int(type_article_id)
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')
    tuple_update = (nom,type_article_id,prix,stock,description,image,id)
    sql = "UPDATE article SET nom=%s, type_article_id=%s,prix=%s,stock=%s,description=%s,image=%s WHERE id = %s;"
    mycursor = get_db().cursor()
    mycursor.execute(sql, tuple_update)
    get_db().commit()
    print(u'article modifié , nom : ', nom, ' - type_article:', type_article_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'article modifié , nom:'+nom + '- type_article:' + type_article_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message)
    return redirect(url_for('admin_article.show_article'))
