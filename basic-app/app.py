from flask import Flask

app = Flask(__name__)  # Flask web server


@app.route("/")  # API function
def hello():
    return "Hello World by Hassan"


if __name__ == "__main__":
    app.run()
