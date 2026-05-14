from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve

import utils

app = Flask(__name__)
cors = CORS(app)


@app.route('/readings', methods=['GET'])
def get_readings():
    word = request.args.get('word')
    return jsonify(utils.generate_readings(word))


if __name__ == '__main__':
    print('LinearA ready!')
    try:
        serve(app,
              host='0.0.0.0',
              port=8080)
    except (KeyboardInterrupt, SystemExit):
        print("Stopping LinearA...")
    finally:
        print('LinearA stopped.')
