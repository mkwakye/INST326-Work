import sqlite3
import pandas as pd

class chinook:
    def __init__(self, path):
        self.path = path
        self.data_tuples = self.get_data()
        self.df = self.create_df()

    def create_df(self): #for dataframe
        """df = pd.DataFrame(iterable)
        print(df)"""
        df = pd.DataFrame(self.data_tuples)
        return df
    
    def get_data(self):
        #conn = sqlite3.connect("chinook.db")
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()

        sql = "SELECT * FROM tracks"

        results = cursor.execute(sql).fetchall()
        
        conn.close()

        return results

if __name__ == '__main__':
    #data = main()
    
    #create_df(data) #for dataframe
    
    """for i in data: # for iterating
        #print(i[1])
        print(i)"""
        
    my_db = chinook("chinook.db")
    print(my_db)