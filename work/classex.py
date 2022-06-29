import sqlite3
import pandas as pd

def create_df(iterable): #for dataframe
    df = pd.DataFrame(iterable)
    print(df)

def main():
    conn = sqlite3.connect("chinook.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM tracks"

    results = cursor.execute(sql).fetchall()
    
    conn.close()

    return results

if __name__ == '__main__':
    data = main()
    
    create_df(data) #for dataframe
    
    """for i in data: # for iterating
        #print(i[1])
        print(i)"""