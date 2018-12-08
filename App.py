from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import pymysql
import os
import Auth
# import Buku

 
app = Flask(__name__)


class Service():
	@app.route('/')
	def home():
		return auth.home()
	@app.route('/daftar')
	def daftar_form():
		return auth.daftar_form()
	@app.route('/UploadBuku')
	def UploadBuku_form():
		return auth.daftar_form()
	@app.route('/login',methods=['POST'])
	def login():
		POST_USERNAME = str(request.form['username'])
		POST_PASSWORD = str(request.form['password'])
 
		return auth.login(POST_USERNAME,POST_PASSWORD)
	@app.route('/mendaftar',methods=['POST'])
	def mendaftar():
		POST_EMAIL	= str(request.form['email'])
		POST_NAMA	= str(request.form['nama'])
		POST_PASSWORD = str(request.form['password'])
 
		return auth.mendaftar(POST_EMAIL,POST_NAMA,POST_PASSWORD)
	@app.route('/logout')
	def logout():
		return auth.logout()
		



if __name__ == "__main__":
	auth = Auth.Auth()
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=4000)