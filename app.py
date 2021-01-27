import flask
import dbfuncs
from flask import request, jsonify, Response
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/getalldata', methods=['GET'])
def getalldata():
    return jsonify(dbfuncs.getallempdata())

@app.route('/getempid/<name>', methods=['GET'])
def getempid(name):
    return jsonify(dbfuncs.getempid(name))

@app.route('/getempdata/<id>', methods=['GET'])
def getempdata(id):
    id = int(id)
    return jsonify(dbfuncs.getempdata(id))

@app.route('/setempdesc', methods=['POST'])
def setempdesc():
    empreq = request.get_json()
    dbfuncs.updatedesc(empreq['id'], empreq['desc'])
    return Response(status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)