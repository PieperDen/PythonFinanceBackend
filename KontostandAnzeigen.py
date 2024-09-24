import mysql.connector as sql
from mysql.connector import Error
from decimal import Decimal
import psycopg2

class getKonto:
    def __init__(self):
        self.kontostand = Decimal('0.00')  
        
    def SQLGetKonto(self):
        resultKonto = self.kontostand  
        try:
            connection = psycopg2.connect(
                host='aws-0-eu-central-1.pooler.supabase.com',        
                user='postgres.jpvtmjvrpafzjvoghojs',  
                password='Dsde22.11.23FD',              
                database='postgres',
                port=6543  
            )
            print("Verbindung erstellt")
            cursor = connection.cursor()
            cursor.execute("""SELECT kontostand FROM konto_transaktionen ORDER BY transaktion_id DESC LIMIT 1""")
            resultKontoDB = cursor.fetchone()
            
            if resultKontoDB:
                resultKonto = Decimal(resultKontoDB[0]) 
            else:
                print("Keine Transaktionen gefunden, Rückgabe des Standardwerts.")
        
        except Error as e:
            print(f"Fehler: {e}")
        
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("Verbindung geschlossen.")
        
        return resultKonto  