from flask import Flask, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return make_response('hola')


@app.route('/usuario', methods=['GET'])
def index():
    return make_response('usuarios')


@app.route('/productos', methods=['GET'])
def index():
    return make_response('productos')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
