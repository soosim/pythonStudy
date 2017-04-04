# -*- coding:utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
	return """<h1>Home</h1>"""

@app.route("/signin",methods=['GET'])
def signin_form():
	return """
		<form action = '/signin' method='post'>
			<p><input type="text" name='username'></p>
			<p><input type="text" name='password'></p>
			<button>tijiao</button>
		</form>
	"""

@app.route("/signin",methods=['POST'])
def signin():
	if request.form['username'] == 'admin' and request.form['password'] == '123456':
		return '<h3>Hello</h3>'
	return '<h3>Bad User</h3>'

if __name__ == '__main__':
	app.run()