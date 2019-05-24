from flask import Flask, Response, Request
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')