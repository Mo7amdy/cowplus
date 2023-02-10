import flask
# database related variables

app = flask.Flask(__name__)

@app.route("/home")
def home():
    return "Connection to MySQL failed"

if __name__ == "__main__":
    app.run()