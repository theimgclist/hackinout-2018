import bottle
from bottle import route, run
from bottle import response


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