# import io
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask import Flask, request, redirect, url_for, session, render_template

from transaktion import transaktion

# from createDiagramm import createDia

import psycopg2


app = Flask(__name__)
CORS(app)

def connectDB():
    connection = psycopg2.connect(
            host='aws-0-eu-central-1.pooler.supabase.com',        
            user='postgres.jpvtmjvrpafzjvoghojs',  
            password='Dsde22.11.23FD',              
            database='postgres',
            port=6543  
        )
    print("Verbindung erstellt")
    cursor = connection.cursor()
    return cursor, connection

@app.route('/getPerson', methods=['GET'])
def getPerson():
    cursor, connection = connectDB()
    cursor.execute("""SELECT * FROM Users""")
    
    userData = cursor.fetchall()

    cursor.execute("""SELECT "Kontostand" FROM Einauszahlungen where "UserID" = {} order by "TransaktionsID" limit 1""".format(userData[0][0]))
    balance = cursor.fetchall()

    cursor.execute("""SELECT "Verwendung" FROM Verwendungen where "UserID" = {}""".format(userData[0][0]))
    verwendungsZweckList = cursor.fetchall()

    connection.commit()
    return jsonify({'id': userData[0][0], 'name': userData[0][6], 'balance': balance[0][0], 'list': verwendungsZweckList[0]})
    

@app.route('/putPerson', methods=['POST'])
def putPerson():
    #SQL Abfrage, die User Daten in der Datenbank updated
    pass

@app.route('/putBuchung', methods=['POST'])
def putBuchung():
    
    data = request.get_json()
    cursor, connection = connectDB()
    UserID = data.get('id')
    status = data.get('Status')
    betrag = data.get('betrag')
    verwendungsid = data.get('Verwendungszweck')

    transaktion_params = {
        'Einzahlung': {'eingang': betrag},
        'Auszahlung': {'abgang': betrag}
    }

    params = transaktion_params.get(status, {})
    params['userID'] = UserID
    params['verwendungsID'] = verwendungsid

    newTransaktion = transaktion(cursor=cursor, connection=connection, **params)

@app.route("/")
def home():
    return "Hier gibt es nichts zu sehen"

@app.route('/login', methods=['POST'])
def login():
    cursor, connection = connectDB()
    data = request.get_json()
    user = data.get('username')
    passwort = data.get('password')
    cursor.execute(f"""SELECT * FROM Users WHERE Passwort = '{passwort}' AND Username = '{user}'""")
    username = cursor.fetchall[0]
    if username == user:
        session['username'] = user
        
        return redirect(url_for('success')) 
    else:
        return redirect(url_for('success')) 
    
    
@app.route('/success')
def success():
    return render_template('index2.html')

    
@app.route('/denied')
def denied():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)