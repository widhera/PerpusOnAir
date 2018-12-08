from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import pymysql
import os
import Auth
import PyPDF2
from werkzeug import secure_filename

 
app = Flask(__name__)


class Service():
	@app.route('/')
	def home():
		return auth.home()
	@app.route('/daftar')
	def daftar_form():
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
 
		return POST_PASSWORD
	@app.route('/logout')
	def logout():
		return auth.logout()
		
	@app.route('/upload', methods = ['GET', 'POST'])
	def upload_file():
	   	if request.method == 'POST':
	   		f = request.files['file']
			f.save(os.path.join(session.get('username'), secure_filename(f.filename)))
			return 'file uploaded successfully'

	@app.route('/file/<nama_file>')
	def readfile(nama_file):
		return render_template('readfile.html',file=nama_file)
		

if __name__ == "__main__":
	auth = Auth.Auth()
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=4000)