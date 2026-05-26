from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve

import db
import utils

app = Flask(__name__)
cors = CORS(app)


@app.route('/readings', methods=['GET'])
def get_readings():
    word = request.args.get('word')
    return jsonify(utils.generate_readings(word))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.Session.remove()


if __name__ == '__main__':
    print('LinearA ready!')
    try:
        serve(app,
              host='0.0.0.0',
              port=8080)
    except (KeyboardInterrupt, SystemExit):
        print("Stopping LinearA...")
    finally:
        db.stop_pool()
        print('LinearA stopped.')
