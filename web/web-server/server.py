import bottle
from bottle import route, run
from bottle import response
from bottle import static_file


# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/')
@enable_cors
def home_page():
    return static_file('index.html', root='./../web-client/')

@route('/css/<cssFile>')
@enable_cors
def serve_css_files(cssFile):
    filePath = './../web-client/css/'
    return static_file(cssFile, filePath)

@route('/js/<jsFile>')
@enable_cors
def serve_js_files(jsFile):
    filePath = './../web-client/js/'
    return static_file(jsFile, filePath)

@route('/hello')
@enable_cors
def hello():
    return "Hello World!"

@route('/newusersignup', method="POST")
@enable_cors
def newusersignup():
    for l in request.body:
        print(l)

@route('/olduserverify', method="POST")
@enable_cors
def olduserverify():
    print("here")
    return "done"

run(host='localhost', port=8080, debug=True)