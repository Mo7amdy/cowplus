import flask
import json
import pymysql.cursors
from datetime import datetime
# database related variables

mysqlHost = "localhost"
dbName = "sensors_data"
mysqlUser = "admin"
mysqlPassword = "SYSTEM123"

app = flask.Flask(__name__)

@app.route("/home")
def home():
    try:
        db = pymysql.connect(host=mysqlHost, user=mysqlUser, password=mysqlPassword, db=dbName, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        db.close()
        return "MySQL Client Connected"
    except:
        sys.exit("Connection to MySQL failed")
        return "Connection to MySQL failed"

if __name__ == "__main__":
    app.run()