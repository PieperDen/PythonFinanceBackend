from decimal import Decimal
import psycopg2

class transaktion:
    def __init__(self, userID,  Name = "Tester", datum = "24-01-01", eingang=0, abgang=0, verwendungszweck="", produkt="Gegenstand"):
        self.produkt = produkt
        self.userID = userID
        self.name = Name
        self.datum = datum
        self.eingang = Decimal(eingang)
        self.abgang = Decimal(abgang)
        self.verwendungszweck = verwendungszweck
        
        
        
    def doTransaktion(self):
        connection = psycopg2.connect(
            host='aws-0-eu-central-1.pooler.supabase.com',        
            user='postgres.jpvtmjvrpafzjvoghojs',  
            password='Dsde22.11.23FD',              
            database='postgres',
            port=6543  
        )
        print("Verbindung erstellt")
        cursor = connection.cursor()
        
        cursor.execute(f"""SELECT "Kontostand" FROM einauszahlungen WHERE "UserID" = {self.userID} ORDER BY "TransaktionsID" DESC LIMIT 1""")
        resultKonto = cursor.fetchone()
        if resultKonto:
            resultKonto = Decimal(resultKonto[0]) 
        else:
            resultKonto = self.kontostand
                
        cursor.execute(f"""SELECT MAX("TransaktionsID") FROM einauszahlungen WHERE "UserID" = {self.userID}""")
        print(cursor.fetchall())
        resultID = cursor.fetchone()
        if resultID[0] is None:
            resultID = 1
        else:
            resultID = resultID[0] + 1
        
        if self.eingang != 0:
            resultKonto += self.eingang
        else:
            resultKonto -= self.abgang
            
        sql_befehl = f"""
        INSERT INTO Users (TransaktionsID, UserID, Kontostand, Einzahlung, Auszahlung, Produkt)
        VALUES ({resultID}, {self.userID}, {resultKonto}, {self.eingang}, {self.abgang}, '{self.produkt}', '{self.name}',  '{self.name}');
        """

      
        cursor.execute(sql_befehl)           
        connection.commit()
        print("Daten erfolgreich eingefügt")
    
    
     
                

  
if __name__ == "__main__":
    connecter = transaktion(userID = 1)
    connecter.doTransaktion()
        
        