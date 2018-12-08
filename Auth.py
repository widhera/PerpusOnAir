
import pymysql
from flask import Flask, flash, redirect, render_template, request, session, abort
import pymysql
import os

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
	    	arr = os.listdir(session.get('username'))
	        return render_template('listdirectory.html',arr=arr)
	def daftar_form(self,alert=''):
		return render_template('daftar.html')

	def login(self,email=None,password=None,mysql=None):
	 	self.email = email
		self.password = hash(password)

		query = "SELECT * from user where email = '"+self.email+"' and password ='"+ str(self.password)+"'"
		print query
		cursor.execute(query)
		result = cursor.fetchall()
		alert=''
		if result:
			session['logged_in'] = True
			session['username'] = str(result[0][2])
			print session['username']
		else:
			alert='Password atau email salah'
		return self.home(alert)
	def logout(self):
		session['logged_in'] = False
		return self.home()