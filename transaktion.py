# from decimal import Decimal
# import psycopg2

# class transaktion:
#     def __init__(self, userID,  Name = "Tester", datum = "24-01-01", eingang=0, abgang=0, verwendungszweck=""):
#         self.userID = userID
#         self.name = Name
#         self.datum = datum
#         self.eingang = Decimal(eingang)
#         self.abgang = Decimal(abgang)
#         self.verwendungszweck = verwendungszweck
        
        
        
#     def doTransaktion(self):
      

#         connection = psycopg2.connect(
#             host='aws-0-eu-central-1.pooler.supabase.com',        
#             user='postgres.jpvtmjvrpafzjvoghojs',  
#             password='Dsde22.11.23FD',              
#             database='postgres',
#             port=6543  
#         )
#         print("Verbindung erstellt")
#         cursor = connection.cursor()
        
#         cursor.execute("""SELECT kontostand FROM Users ORDER BY transaktion_id DESC LIMIT 1""")
#         resultKonto = cursor.fetchone()
#         if resultKonto:
#             resultKonto = Decimal(resultKonto[0]) 
#         else:
#             resultKonto = self.kontostand
                
#         cursor.execute("""SELECT MAX("TransaktionsID") FROM einauszahlungen""")
#         print(cursor.fetchall())
#         resultID = cursor.fetchone()
#         if resultID[0] is None:
#             resultID = 1
#         else:
#             resultID = resultID[0] + 1
        
#         if self.eingang != 0:
#             resultKonto += self.eingang
#         else:
#             resultKonto -= self.abgang
            
#         sql_befehl = f"""
#         INSERT INTO Users (TransaktionsID, UserID, first_name, last_name, EMail, Passwort, Username)
#         VALUES ({self.}, {self.userID}, {self.name}, {self.name}, '{self.name}', '{self.name}',  '{self.name}');
#         """

      
#         cursor.execute(sql_befehl)           
#         connection.commit()
#         print("Daten erfolgreich eingefügt")
    
    
     
                

  
# if __name__ == "__main__":
#     connecter = transaktion()
#     connecter.doTransaktion()
        
        