from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory, url_for
import pymysql
import os
import Auth
import PyPDF2
from werkzeug import secure_filename
import shutil

 
app = Flask(__name__)

db = pymysql.connect("localhost", "root", "", "perpusonair")
cursor = db.cursor()

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
		POST_EMAIL = str(request.form['email'])
		POST_NAMA = str(request.form['nama'])
		POST_PASSWORD = str(hash(request.form['password']))
		print POST_PASSWORD
 		
		query = "INSERT INTO user (`email`,`nama`,`password`,`memory`) values ('"+POST_EMAIL+"','"+POST_NAMA+"','"+POST_PASSWORD+"',1000000000)"
		cursor.execute(query)
		db.commit()

		id_user=str(cursor.lastrowid)
		query = "INSERT INTO buku (`id_user`,`judul`,`path`,`ukuran`) values ("+id_user+",'/','/"+id_user+"',0)"
		cursor.execute(query)
		db.commit()		
		return redirect('/')
	@app.route('/logout')
	def logout():
		return auth.logout()
	
	@app.route('/index/<id_buku>')
	def index(id_buku):
		if not session.get('logged_in'):
			return render_template('login.html',alert='')
		query = "SELECT * from buku where id = '"+id_buku+"'"
		cursor.execute(query)
		result = cursor.fetchall()

		path_root = str(result[0][3])
		arr = os.listdir('static\\bookshelf\\'+str(result[0][3]))
		my_list = []
		for i in arr:
			path_temp = str(path_root)+'/'+i
			query = "SELECT * from buku where `path`  = '"+path_temp+"'"
			
			cursor.execute(query)
			result = cursor.fetchall()

			path_temp = 'static\\bookshelf\\'+path_root+"\\"+str(i)
			path_temp = path_temp.replace('/','\\')
			
			if(os.path.isdir(path_temp)):
				direct='DIR'
			else:
				direct=''
			print result
			arr_i = [result[0][0],result[0][2],result[0][4],direct]
			my_list.append(arr_i)
		query = "SELECT sum(ukuran) from buku where `id_user`  = '"+session.get('id')+"'"
	
		cursor.execute(query)
		result = cursor.fetchall()
		return render_template('main.html',arr=my_list,space=session.get('space'), used=result[0][0])

	@app.route('/upload', methods = ['GET', 'POST'])
	def upload_file():
		if not session.get('logged_in'):
			return render_template('login.html',alert='')
	   	if request.method == 'POST':
	   		f = request.files['file']
			f.save( os.path.join('static','bookshelf',session.get('id'), secure_filename(f.filename)))

			id_user = session.get('id')
			judul = f.filename.rsplit('.', 1)[0]
			path = "/"+session.get('id')+"/"+f.filename
			f.seek(0, os.SEEK_END)
			ukuran =  str(f.tell())
			print ukuran
			query = "INSERT INTO buku (`id_user`,`judul`,`path`,`ukuran`) values ("+id_user+",'"+judul+"','"+path+"',"+ukuran+")"
			print query
			cursor.execute(query)
			db.commit()
		return redirect(url_for('index',id_buku=session.get('root_id') ))

	@app.route('/readfile/<id_buku>')
	def readfile(id_buku):
		if not session.get('logged_in'):
			return render_template('login.html',alert='')

		query = "SELECT * from buku where `id`  = '"+id_buku+"'"
		print query
		cursor.execute(query)
		result = cursor.fetchall()

		path = result[0][3].replace('/','\\')
		data = '\\static\\bookshelf'+path
		return render_template('read.html',data=data, nama_file=result[0][2])

	@app.route('/delete/<id_buku>')
	def delete(id_buku):
		if not session.get('logged_in'):
			return render_template('login.html',alert='')

		query = "SELECT * from buku where `id`  = '"+id_buku+"'"
		print query
		cursor.execute(query)
		result = cursor.fetchall()

		path = result[0][3].replace('/','\\')
		data = 'static\\bookshelf'+path
		print ("tayar"+data)
		if os.path.exists(data):
  			
  			if(os.path.isdir(data)):
  				shutil.rmtree(data)
  			else:
  				os.remove(data)
  			query = "DELETE from buku where `id`  = '"+id_buku+"'"
			print query
			cursor.execute(query)
			db.commit()
		return redirect(url_for('index',id_buku=session.get('root_id') ))

	@app.route('/newFile',methods=['POST'])
	def newFile():
		if not session.get('logged_in'):
			return render_template('login.html',alert='')

		POST_NAMA_FILE	= str(request.form['namafile'])
		POST_PATH	= str(request.form['path'])

		id_user = session.get('id')
		judul = POST_NAMA_FILE.rsplit('.', 1)[0]
		path = "/"+session.get('id')+POST_PATH+POST_NAMA_FILE
		ukuran = "0"

		data= path.replace('/','\\')
		data = 'static\\bookshelf'+data
		if not os.path.exists(data):
  			query = "INSERT INTO buku (`id_user`,`judul`,`path`,`ukuran`) values ("+id_user+",'"+judul+"','"+path+"',"+ukuran+")"
			print query
			cursor.execute(query)
			db.commit()
			open(data, 'a').close()
		return redirect(url_for('index',id_buku=session.get('root_id') ))

	@app.route('/newFolder',methods=['POST'])
	def newFolder():
		if not session.get('logged_in'):
			return render_template('login.html',alert='')

		POST_NAMA_FOLDER	= str(request.form['namafolder'])
		POST_PATH	= str(request.form['path'])

		id_user = session.get('id')
		judul = POST_NAMA_FOLDER
		path = "/"+session.get('id')+POST_PATH+POST_NAMA_FOLDER
		ukuran = "0"

		data= path.replace('/','\\')
		data = 'static\\bookshelf'+data
		if not os.path.exists(data):
  			query = "INSERT INTO buku (`id_user`,`judul`,`path`,`ukuran`) values ("+id_user+",'"+judul+"','"+path+"',"+ukuran+")"
			print query
			cursor.execute(query)
			db.commit()
			os.makedirs(data)
		return redirect(url_for('index',id_buku=session.get('root_id') ))

	@app.route('/movePath',methods=['POST'])
	def movePath():
		if not session.get('logged_in'):
			return render_template('login.html',alert='')

		POST_ID_BUKU	= str(request.form['idBuku'])
		POST_PATH	= str(request.form['path'])

		query = "SELECT * from buku where `id`  = '"+POST_ID_BUKU+"'"
		print query
		cursor.execute(query)
		result = cursor.fetchall()

		nama_file = result[0][3].rsplit('/', 1)[1]
		path = result[0][3].replace('/','\\')
		source_path = 'static\\bookshelf'+path

		data = POST_PATH.replace('/','\\')
		target_path = 'static\\bookshelf\\'+session.get('id')+data

		if os.path.exists(source_path):
			print("tagetpath required")
			if(os.path.isdir(source_path)):
				shutil.copytree(source_path, target_path)
				shutil.rmtree(source_path)
				POST_PATH = '/'+session.get('id')+POST_PATH.rsplit('/', 1)[0]
				POST_PATH2 = result[0][3]
				query = "update buku set path = replace(path,'"+POST_PATH2+"', '"+POST_PATH+"') where path like '%"+POST_PATH2+"%'"
				print query
				cursor.execute(query)
				db.commit()
			else:
				query = "UPDATE buku set `path` = '"+'/'+session.get('id')+POST_PATH+nama_file+"' where id = "+POST_ID_BUKU+""
				print query
				cursor.execute(query)
				db.commit()
				shutil.move(source_path, target_path)

		return redirect(url_for('index',id_buku=session.get('root_id') ))

	@app.route('/upgrade')
	def upgrade():
		if not session.get('logged_in'):
			return render_template('login.html',alert='')

		query = "update user set memory = 5000000000 where id="+str(session.get('root_id'))
		session['space'] = '5000000000'
		cursor.execute(query)
		db.commit()

		return redirect(url_for('index',id_buku=session.get('root_id') ))


if __name__ == "__main__":
	auth = Auth.Auth()
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=4000)