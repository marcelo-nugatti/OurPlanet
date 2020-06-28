from django.test import TestCase

# Create your tests here.

class Burn():
    def __init__(self):
        self.earth = 9.807
        self.marth = 3.711
    
    def weightEarth(self):
        self.weight = float(input("Ingresa tu peso: "))

    def algorithm(self):
        #(peso/g.tierra)*g.marte

        result = (self.weight / self.earth) * self.marth
        print(f"Tu peso en Marte es de: {result}.kg")






if __name__ == '__main__':
    app = Burn()
    app.weightEarth()
    app.algorithm()



