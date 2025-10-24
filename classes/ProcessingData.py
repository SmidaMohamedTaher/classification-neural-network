import pandas as pd
class ProcessingData :
    @staticmethod
    def geCsvtData(path):
        return pd.read_csv(path)
    
    @staticmethod
    def getCsvData(path,sp):
        return pd.read_csv(path, sep=sp)
    
    @staticmethod
    def hotCoding(df):
        df = df.replace({"yes": 1, "no": 0})
        string_columns = df.select_dtypes(include=["object"]).columns
        return pd.get_dummies(df,columns=string_columns,dtype=int)