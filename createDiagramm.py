# import matplotlib
# matplotlib.use('Agg')  
# import matplotlib.pyplot as plt
# from getDiaFiles import getDia


# class createDia:
    
#     def __init__(self):
#         self.dia = getDia(5)
#         self.y = self.dia.getData()
#         self.x = range(len(self.y))
    
    
#     def createDia(self):
        
#         print(self.y)
#         plt.plot(self.x, self.y)
        
#         for i in range(len(self.y)):
#             if self.y[i] < 0:  
#                 plt.scatter(self.x[i], self.y[i], color='red', s=100, label=f"Markierter Punkt {i}")
                
#             elif self.y[i] % 100 == 0:
#                 plt.scatter(self.x[i], self.y[i], color='green', s=100, label=f"Markierter Punkt {i}")
                 
            
            
#         plt.savefig("C:\\Users\\P027161\\OneDrive - Provinzial\\Desktop\\Finanztool\\Statistiken\\Statistik.png")
#         return plt



# if __name__ == "__main__":
#     dia = createDia()
#     dia.createDia()