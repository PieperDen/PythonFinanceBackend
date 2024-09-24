# import io
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
# from transaktion import transaktion
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

# @app.route('/api/data', methods=['POST'])
# def post_data():

#     data = request.json  
    
#     betrag = data.get('Betrag')
#     verwendung = data.get('verwendung')
    
#     if verwendung == "Einzahlung":
#         tran = transaktion(eingang=betrag, verwendungszweck="Geld wurde eingezahlt")
#         tran.doTransaktion()
#     else:
#         tran = transaktion(abgang=betrag, verwendungszweck="Geld wurde ausgezahlt")
#         tran.doTransaktion()
        
    
#     return jsonify({'received': data})

#Brauchst du eig nicht
# @app.route('/getKontostand')
# def getKontostand():
#     konto = getKonto()
#     result = konto.SQLGetKonto()
#     return jsonify({'kontostand': result})

@app.route('/getPerson', methods=['GET'])
def getPerson():
    cursor, connection = connectDB()
    cursor.execute("""SELECT * FROM Users""")
    
    userData = cursor.fetchall()
    
    #Bsp:
    # id = 1
    # name = "Max Mustermann"
    # balance = 1000
    # verwendungsZweckList = ['Einzahlung', 'Auszahlung']

    #SQL Abfrage, die User Daten aus der Datenbank holt

    #return jsonify({'id': userData[0][0], 'name': user[0][6], 'balance': balance, 'list': verwendungsZweckList})
    connection.commit()
    return jsonify({'received': cursor.fetchall()})

@app.route('/putPerson', methods=['POST'])
def putPerson():
    #SQL Abfrage, die User Daten in der Datenbank updated
    pass

@app.route('/putBuchung', methods=['POST'])
def putBuchung():
    #SQL Abfrage, die Buchung in der Datenbank updated
    #Daten: ID, Betrag, Verwendungszweck, Status(Einzahlung/Auszahlung)
    pass
    

# @app.route('/getImage')
# def createDiagramm():
#     diag = createDia()
#     buf = io.BytesIO()
#     diag.createDia().savefig(buf, format="png")
#     buf.seek(0)
    
#     return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)