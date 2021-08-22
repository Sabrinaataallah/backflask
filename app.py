from flask import *
from flask_mysqldb import MySQL
from flask_cors import CORS
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = "Secret key"
app.config['SECRET_KEY'] = 'Secret Key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'personne'
mysql = MySQL(app)


@app.route('/listepersonne',methods=['get'])
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user ")
    fetchuser = cur.fetchall()
    cur.close()

    return json.dumps(fetchuser)






if __name__ == '__main__':
    app.run()
