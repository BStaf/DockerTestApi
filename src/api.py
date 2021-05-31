import flask
from flask import request, jsonify
#from random import seed
from random import randint

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

#seed(1)
data = {"v1 data":randint(0,1000)}

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/data', methods=['GET'])
def get_id():
    return jsonify(data)

app.run(host='0.0.0.0')
