from flask import Flask
from flask_cors import CORS
from controller import server_blueprint

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})

app.register_blueprint(server_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)