from decimal import Decimal
import psycopg2
import hashlib

class transaktion:
    def __init__(self, cursor, connection, userID,  Name = "Tester", datum = "24-01-01", eingang=0, abgang=0, verwendungszweck="", produkt="Gegenstand", verwendungsID = 1):
        self.cursor = cursor
        self.connection = connection
        self.verwendungsid = verwendungsID
        self.produkt = produkt
        self.userID = userID
        self.name = Name
        self.datum = datum
        self.eingang = Decimal(eingang)
        self.abgang = Decimal(abgang)
        self.verwendungszweck = verwendungszweck
        
        
        
    def doTransaktion(self):
        print("Verbindung erstellt")
       
        
        self.cursor.execute(f"""SELECT "Kontostand" FROM einauszahlungen WHERE "UserID" = {self.userID} ORDER BY "TransaktionsID" DESC LIMIT 1""")
        resultKonto = self.cursor.fetchone()
        if resultKonto:
            resultKonto = Decimal(resultKonto[0]) 
        else:
            resultKonto = self.kontostand
                
        self.cursor.execute(f"""SELECT MAX("TransaktionsID") FROM einauszahlungen WHERE "UserID" = {self.userID}""")
        resultID = self.cursor.fetchone()
        if resultID is None or resultID[0] is None:
            resultID = 1
        else:
            resultID = resultID[0] + 1
        
        if self.eingang != 0:
            resultKonto += self.eingang
        else:
            resultKonto -= self.abgang
            
        sql_befehl = f"""
        INSERT INTO einauszahlungen ("TransaktionsID", "UserID", "Kontostand", "Einzahlung", "Auszahlung", "Produkt", "VerwendungsID")
        VALUES ({resultID}, {self.userID}, {resultKonto}, {self.eingang}, {self.abgang}, '{self.produkt}', {self.verwendungsid});
        """

      
        self.cursor.execute(sql_befehl)           
        self.connection.commit()
        print("Daten erfolgreich eingefügt")
        
        
    def saveUser(self, UserID, passwort, Username, first_name, last_name, Email, Bio="Ein dankbarer User"):
        hashesdpasswort = hashlib.sha256(passwort.encode()).hexdigest()
        
        
        sql_befehl = f"""
        INSERT INTO users ("UserID", "first_name", "last_name", "EMail", "Passwort", "Username", "Bio")
        VALUES ({UserID}, {first_name}, {last_name}, {Email}, {hashesdpasswort}, '{Username}', {Bio});
        """

        self.cursor.execute(sql_befehl)    
        

    
     
                

  
if __name__ == "__main__":
    connecter = transaktion(userID = 1)
    connecter.doTransaktion()
        
        