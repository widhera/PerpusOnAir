
import pymysql
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import pymysql
import os

db = pymysql.connect("localhost", "root", "yoza", "perpusonair")
cursor = db.cursor()

class Auth(object):
	def __init__(self):
		self.email = ''
		self.password = ''
	def home(self,alert=''):
	    if not session.get('logged_in'):
	        return render_template('login.html',alert=alert)
	    else:
	    	return redirect(url_for('index',id_buku=session.get('root_id') ))
	def daftar_form(self,alert=''):
		return render_template('daftar.html')

	def login(self,email=None,password=None,mysql=None):
		if not session.get('logged_in'):
			self.email = email
			self.password = password

			query = "SELECT * from user where email = '"+self.email+"' and password ='"+ str(self.password)+"'"
			print query
			cursor.execute(query)
			result = cursor.fetchall()
			alert=''
			if result:
				session['logged_in'] = True
				session['id'] = str(result[0][0])
				session['username'] = str(result[0][2])
				session['root_id'] = result[0][5]
				session['space'] = result[0][4]
			else:
				alert='Password atau email salah'
			return self.home(alert)
		else:
			return self.home()
	def logout(self):
		session['logged_in'] = False
		return self.home()
