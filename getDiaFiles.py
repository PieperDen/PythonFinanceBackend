import mysql.connector as sql
from mysql.connector import Error
from decimal import Decimal
from supabase import create_client, Client


class getDia:
    
    def __init__(self, DataArt):
        self.DataArt = DataArt
    

    def getData(self):
        try:
            connection = sql.connect(
                host='aws-0-eu-central-1.pooler.supabase.com',        
                user='postgres.jpvtmjvrpafzjvoghojs',    
                password='Dsde22.11.23FD',              
                database='postgres' 
            )
            print("Verbindung erstellt")
            cursor = connection.cursor()
            cursor.execute("""SELECT kontostand FROM konto_transaktionen ORDER BY transaktion_id""")
            resultKontoDB = cursor.fetchall()
            resultKontoDB = [Decimal(item[0]) for item in resultKontoDB]
            
                
        
        except Error as e:
            print(f"Fehler: {e}")
        
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("Verbindung geschlossen.")
        
        return resultKontoDB  
    
    
    
  