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


@app.route('/')
def home():
   # cur = mysql.connection.cursor()
   # cur.execute("CREATE TABLE example (id INTEGER , name VARCHAR (20), lastname VARCHAR(20) )")
    #cur.execute("INSERT INTO example VALUES (1,'SAB','dfvv')")
   # cur.execute("INSERT INTO example VALUES (2,'SAffB','hgh')")
   # cur.execute("INSERT INTO example VALUES (3,'SfdfAffB','gfjg')")
    #mysql.connection.commit()
    return 'Done'

@app.route('/listepersonne',methods =['GET'])
def liste():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user ")
    fetchuser = cur.fetchall()
    cur.close()

    return json.dumps(fetchuser)

@app.route('/insertpersonne' , methods = ['POST'] )
def insert():
    civilite = request.json['civilite']
    Nom = request.json['Nom']
    Prenom = request.json['Prenom']
    Date_de_naissance= request.json['Date_de_naissance']
    Situation_familiale= request.json['Situation_familiale']
    Nb_enfants= request.json['Nb_enfants']
    Email= request.json['Email']
    Tel= request.json['Tel']
    D_Tel= request.json['D_Tel']
    Mobile= request.json['Mobile']
    Adresse= request.json['Adresse']
    Pays= request.json['Pays']
    Ville= request.json['Ville']
    Rue= request.json['Rue']
    N_Rue= request.json['N_Rue']
    Code_Postal= request.json['Code_Postal']
    C_adresse= request.json['C_adresse']
    M_cle= request.json['M_cle']
    comment = request.json['comment']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user (civilite,Nom,Prenom,Date_de_naissance,Situation_familiale,Nb_enfants,Email,Tel,D_Tel,Mobile,Adresse,Pays,Ville,Rue,N_Rue,Code_Postal,C_adresse,M_cle,comment) VALUES (%s,%s,%s, %s ,%s,%s,%s,%s, %s ,%s,%s,%s,%s, %s ,%s,%s,%s,%s, %s)",
                (civilite, Nom, Prenom, Date_de_naissance, Situation_familiale, Nb_enfants, Email, Tel, D_Tel, Mobile, Adresse, Pays, Ville, Rue, N_Rue, Code_Postal, C_adresse, M_cle, comment))
    mysql.connection.commit()
    cur.close()

    return ('succes add')


if __name__ == '__main__':
    app.run()
