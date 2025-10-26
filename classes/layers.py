import random 

class Layers:
    @staticmethod
    def generateWidth(num):
        list = []
        for i in range(num):
            list.append(round(random.uniform(-1, 1), 1))
    
        return list 
    @staticmethod
    def generateLayer(num,num2):
        list = []
        for i in range(num):
            list.append(Layers.generateWidth(num2))
        return list 