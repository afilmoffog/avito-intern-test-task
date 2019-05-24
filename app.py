from flask import Flask, Response, request
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import shell_scripts


app = Flask(__name__)
main_path = '/api/v1'

@app.route('/')
def index():
    return Response("try another path")

@app.route(main_path+'/get_rabbit', methods=['GET'])
def get_rabbit():
    return Response(shell_scripts.RABBITMQ_SCRIPT, mimetype='text/plan') 

@app.route(main_path+'/get_mongo', methods=['GET'])
def get_mongo():
    return Response(shell_scripts.MONGO_SCRIPT, mimetype='text/plan')

@app.route(main_path + '/test_mongo', methods=['GET'])
def test_mongo():
    host, port = request.args.get('host', default='localhost'), request.args.get('port', default='27017')
    uri = "mongodb://%s:%s/admin" % (host, port)
    client = MongoClient(uri, maxPoolSize=1, connectTimeoutMS=3000, serverSelectionTimeoutMS=3000)
    resp = Response('false', mimetype='text/plain')
    try:
        if client.admin.command('ismaster')['ok'] == 1:
            resp = Response('true', mimetype='text/plain')
    except ConnectionFailure:
        resp = Response('false', mimetype='text/plain')

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')