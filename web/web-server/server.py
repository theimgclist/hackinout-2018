import bottle
from bottle import route, run
from bottle import response, request
from bottle import static_file
import base64
import binascii
import base64
import pickle
import io
import os
import sys
from shutil import copyfile
import uuid
import json

globalFileName = "lalalala";
globalCommonDB = {};

def getGlobalFileName():
    global globalFileName    # Needed to modify global copy of globvar
    return globalFileName

def setGlobalFileName(filename):
    global globalFileName    # Needed to modify global copy of globvar
    globalFileName = filename

def addUserToDB(userID):
	

def deductBalanceFromDB(userID):


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

@route('/payment')
@enable_cors
def payment_page():
    return static_file('payment.html', root='./../web-client/')    

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

@route('/newusersignupimage', method="POST")
@enable_cors
def newusersignupimage():
    print("Entered newusersignupimage")
    postdata = request.body.read()
    file = open('xyz.jpg','wb')
    file.write(postdata)
    file.close
    myfile = open('xyz.jpg', 'r')
    a = myfile.read()
    myfile.close()
    #print(a)
    i = a.find(',')
    #print(i)
    a = a[i+1:]
    print(a[0])
    #print(type(a))
    import base64
    imgdata = base64.b64decode(a)
    #print(imgdata)
    filename = getGlobalFileName()+'.jpg'  # I assume you have a way of picking unique filenames
    print("filename: "+filename)
    f = open(filename, 'wb')
    f.write(imgdata)
    f.close()
    copyfile(filename,"./database/"+filename)	
    
@route('/newuserdata', method="POST")
@enable_cors
def newuserdata():
    filename = str(uuid.uuid4());
    setGlobalFileName(filename);
    print("Entered newuserdata")
    postdata = request.body.read()
    print(postdata)	


@route('/verifyIdentityForPayment', method="POST")
@enable_cors
def verifyIdentityForPayment():
    print("Entered verifyIdentityForPayment")
    postdata = request.body.read()
    file = open('xyz.jpg','wb')
    file.write(postdata)
    file.close
    myfile = open('xyz.jpg', 'r')
    a = myfile.read()
    myfile.close()
    #print(a)
    i = a.find(',')
    #print(i)
    a = a[i+1:]
    print(a[0])
    #print(type(a))
    import base64
    imgdata = base64.b64decode(a)
    print(imgdata)
    filename = str(uuid.uuid4())+'.jpg'  # I assume you have a way of picking unique filenames
    print("filename: "+filename)
    f = open(filename, 'wb')
    f.write(imgdata)
    f.close()
    #copyfile("D:\\Projects\\HackInOut\\hackinout-2018-master\\web\\web-server\\"+filename,"D:\\Projects\\FaceDetectionFromBlog\\facematch\\checkin\\"+filename)
    #os.remove("./"+filename)
    #os.remove("./xyz.jpg")
	#print(len(postdata))
    #ime = image.open(io.BytesIO(lala))
    #ime.save('./abcd.jpg')
	#a = D:\Projects\FaceDetectionFromBlog\facematch\launch.py
    #path = "D:\\Projects\\FaceDetectionFromBlog\\facematch\\"
    #os.chdir(path)
    #print(os.getcwd())
    #sys.path.insert(0, r"D:\Projects\FaceDetectionFromBlog\facematch")
    #import launch
    match = -1
    userID = 1
    #match = launch.match(filename)
    print("tadawwwwwwwww",match)
    if match == -1:
        return "-1"
    else:
    	deductBalanceFromDB(userID)
        os.remove("D:\\Projects\\HackInOut\\hackinout-2018-master\\web\\web-server\\"+filename)
        return "Match found"


@route('/olduserverify', method="POST")
@enable_cors
def olduserverify():
    print("Entered olduserverify")
    postdata = request.body.read()
    file = open('xyz.jpg','wb')
    file.write(postdata)
    file.close
    myfile = open('xyz.jpg', 'r')
    a = myfile.read()
    myfile.close()
    #print(a)
    i = a.find(',')
    #print(i)
    a = a[i+1:]
    print(a[0])
    #print(type(a))
    import base64
    imgdata = base64.b64decode(a)
    print(imgdata)
    filename = str(uuid.uuid4())+'.jpg'  # I assume you have a way of picking unique filenames
    print("filename: "+filename)
    f = open(filename, 'wb')
    f.write(imgdata)
    f.close()
    #copyfile("D:\\Projects\\HackInOut\\hackinout-2018-master\\web\\web-server\\"+filename,"D:\\Projects\\FaceDetectionFromBlog\\facematch\\database\\"+filename)
    #os.remove("./"+filename)
    #os.remove("./xyz.jpg")
	#print(len(postdata))
    #ime = image.open(io.BytesIO(lala))
    #ime.save('./abcd.jpg')
	#a = D:\Projects\FaceDetectionFromBlog\facematch\launch.py
    #path = "D:\\Projects\\FaceDetectionFromBlog\\facematch\\"
    #os.chdir(path)
    #print(os.getcwd())
    #sys.path.insert(0, r"D:\Projects\FaceDetectionFromBlog\facematch")
    #import launch
    match = -1
    #match = launch.match(filename)
    print("tadawwwwwwwww",match)
    if match == -1:
        return "-1"
    else:
        copyfile("D:\\Projects\\FaceDetectionFromBlog\\facematch\\database\\"+filename,"D:\\Projects\\FaceDetectionFromBlog\\facematch\\checkin\\"+filename)
        return "Match found"

run(host='localhost', port=8080, debug=True)