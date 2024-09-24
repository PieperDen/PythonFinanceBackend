# import io
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
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

    #Bsp:
    # id = 1
    # name = "Max Mustermann"
    # balance = 1000
    # verwendungsZweckList = ['Einzahlung', 'Auszahlung']

    connection.commit()
    return jsonify({'id': userData[0][0], 'name': userData[0][6], 'balance': balance[0][0], 'list': verwendungsZweckList[0]})
    

@app.route('/putPerson', methods=['POST'])
def putPerson():
    #SQL Abfrage, die User Daten in der Datenbank updated
    pass

@app.route('/putBuchung', methods=['POST'])
def putBuchung():
    #SQL Abfrage, die Buchung in der Datenbank updated
    #Daten: ID, Betrag, Verwendungszweck, Status(Einzahlung/Auszahlung)
    cursor, connection = connectDB()
    
    newTransaktion = transaktion(cursor=cursor, connection=connection)
    

if __name__ == '__main__':
    app.run(debug=True)