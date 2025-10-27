import numpy as np

class Cal:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x)) 
    
    @staticmethod
    def calculOutput1(df, num, layer1):
        
        row = df.drop(columns=['y']).iloc[num].to_numpy()  
        layer1 = np.array(layer1)  
        
        
        output = np.dot(layer1, row)  
        
        return output.tolist()
        
    @staticmethod
    def calculOutput2(list , layer2):
        output = []
        one = []
        for j in range(1):
            for i in range(16):
                one.append(list[i] * layer2[j][i])
            output.append(sum(one))
            one.clear()
        if len(output) == 1:
            y = Cal.sigmoid(output[0])
            return 1 if y >= 0.5 else 0
        return output 
    
    @staticmethod    
    def calAll(df,layer1,layer2):
        num = df.shape[0]
        out = []
        list = []
        for i in range(num):
            list = Cal.calculOutput1(df,i,layer1)
            out.append(Cal.calculOutput2(list,layer2))
        return out 
