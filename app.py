import io
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from transaktion import transaktion
from KontostandAnzeigen import getKonto
from createDiagramm import createDia


app = Flask(__name__)
CORS(app)


    
    

@app.route('/api/data', methods=['POST'])
def post_data():

    data = request.json  
    
    betrag = data.get('Betrag')
    verwendung = data.get('verwendung')
    
    if verwendung == "Einzahlung":
        tran = transaktion(eingang=betrag, verwendungszweck="Geld wurde eingezahlt")
        tran.doTransaktion()
    else:
        tran = transaktion(abgang=betrag, verwendungszweck="Geld wurde ausgezahlt")
        tran.doTransaktion()
        
    
    return jsonify({'received': data})


@app.route('/getKontostand')
def getKontostand():
    konto = getKonto()
    result = konto.SQLGetKonto()
    return jsonify({'kontostand': result})
    

@app.route('/getImage')
def createDiagramm():
    diag = createDia()
    buf = io.BytesIO()
    diag.createDia().savefig(buf, format="png")
    buf.seek(0)
    
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)