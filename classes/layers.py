import random 

class Layers:
    @staticmethod
    def generateWeight(num):
        list = []
        for i in range(num):
            list.append(round(random.uniform(-0.1, 0.1), 1))
    
        return list 
    @staticmethod
    def generateLayer(num,num2):
        list = []
        for i in range(num):
            list.append(Layers.generateWeight(num2))
        return list 