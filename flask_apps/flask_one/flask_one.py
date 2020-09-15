import requests

from flask import Flask

app = Flask(__name__)


@app.route("/hello", methods=["GET", "POST"])
def hello():
    # requests.post(url, data=None, json=None, **kwargs)
    data = "Hello!"
    url = 'http://localhost:4000/hi'
    r = requests.post(url, data=data)
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
