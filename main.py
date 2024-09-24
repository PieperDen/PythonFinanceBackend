from app import MyApp
from Pythonlogik.transaktion import addEinzahlung
help(addEinzahlung)
#MAIN WIRD IM MOMENT NICHT VERWENDET ):
class Main:
    def __init__(self):
        
        self.total_amount = 0  
        self.app = MyApp(self)  
        print(self.name_list)

    def process_name_and_amount(self, verwendung, amount):
        self.Einzahlung = addEinzahlung(amount, verwendungszweck=verwendung)
        print(f'Name {verwendung} hinzugefügt und Betrag {amount} aktualisiert.')

    def start(self):
        
        self.app.run()

if __name__ == '__main__':
    main_instance = Main()
    main_instance.start()