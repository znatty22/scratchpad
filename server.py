from libs.bottle import route, run, static_file
import os

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8081
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
print ROOT_DIR

def main():
	run(host=DEFAULT_HOST,port=DEFAULT_PORT, debug=True)
		
@route('/')
def home():
	return static_file('index.html',root=ROOT_DIR + '/static')

@route('/main')
def main_content():
	return static_file('main.html',root=ROOT_DIR + '/static')	
	
@route('/libs/js/<filename>')
def serve_js(filename):
	return static_file(filename,root=ROOT_DIR + '/libs/js')	
	
@route('/static/<filename:path>')	
def serve_static(filename):
	return static_file(filename,root=ROOT_DIR + '/static')

@route('/static/css/<filename>')	
def serve_css(filename):
	return static_file(filename,root=ROOT_DIR + '/static/css')

@route('/static/less/<filename>')	
def serve_less(filename):
	return static_file(filename,root=ROOT_DIR + '/static/less')
	
@route('/static/fonts/<filename>')
def serve_font(filename):
	return static_file(filename,root=ROOT_DIR + '/static/fonts')
	
@route('/static/img/<filename>')
def serve_img(filename):
	return static_file(filename,root=ROOT_DIR + '/static/img')

if __name__ == '__main__':
	main()