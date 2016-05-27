from flask import Flask
app = Flask(__name__)

@app.route('/')				#http://127.0.0.1:5000/
def index():
	return 'Index Page'

@app.route('/hello')		#http://127.0.0.1:5000/hello
def hello():
	return 'Hello World'
	
if __name__ =='__main__':
	app.run()