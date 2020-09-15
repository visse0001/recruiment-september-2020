from flask import Flask, request

app = Flask(__name__)


@app.route("/hi", methods=["GET", "POST"])
def hi():
    data = request.data
    return f'{data}, Hi!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
