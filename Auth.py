
import pymysql
from flask import Flask, flash, redirect, render_template, request, session, abort
import pymysql

db = pymysql.connect("localhost", "root", "", "perpusonair")
cursor = db.cursor()

class Auth(object):
	def __init__(self):
		self.email = ''
		self.password = ''
	def home(self,alert=''):
	    if not session.get('logged_in'):
	        return render_template('login.html',alert=alert)
	    else:
	        return "Hello Boss!  <a href='/logout'>Logout</a>"
	def daftar_form(self,alert=''):
		return render_template('daftar.html',alert=alert)

	def login(self,email=None,password=None,mysql=None):
	 	self.email = email
		self.password = hash(password)

		query = "SELECT id from user where email = '"+self.email+"' and password ='"+ str(self.password)+"'"
		print query
		cursor.execute(query)
		result = cursor.fetchall()
		alert=''
		if result:
			session['logged_in'] = True
		else:
			alert='Password atau email salah'
		return self.home(alert)


	def mendaftar(self,email=None,nama=None,password=None):
		alert=''
		query = "SELECT id from user where email = '"+email+"'"
		cursor.execute(query)
		result = cursor.fetchall()
		if len(result)>1:
			alert='Email sudah digunakan'
			return self.daftar_form(alert)	
		else:
			query = "SELECT max(id)+1 as id from user"
			cursor.execute(query)
			result = cursor.fetchone()
			query = "INSERT INTO USER values ('"+str(result[0])+"','"+email+"','"+nama+"','"+str(hash(password))+"','5000',CURRENT_TIME())"
			cursor.execute(query)
			db.commit()
			alert = "Akun berhasil di buat"
		return self.home(alert)

	def logout(self):
		session['logged_in'] = False
		return self.home()