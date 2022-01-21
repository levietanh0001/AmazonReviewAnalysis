from json.tool import main
import pandas as pd
from pandas.io import sql
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker





# df22.to_sql(con=database_connection, name='university_dataset_ca', if_exists='append',chunksize=100)
# database_connection.close()

class DfToMySQL:
    def __init__(self, db, host, user, passwd, port, charset='utf8'):
        self.db = db
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.charset = charset
    def set_dataframe(self, path):
        self.path = path
        self.df = pd.read_csv(self.path, encoding="utf-8-sig")
    def to_mysql(self, table_name='table_name'):
        self.table_name = table_name
        self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.passwd}@{self.host}:{self.port}/{self.db}')
        self.df.to_sql(name=self.table_name, con=self.engine.connect(), if_exists = 'replace', index=False)        
    def print_sample_df(self, row=20):
        print(self.df.head(row))
    def execute_query(self, query=''):
        self.query = query
        self.con = self.engine.connect()
        self.con.execute(query)
        # self.cursor = self.con.cursor()


if __name__ == '__main__': 
    db = 'canned_coffee_5star_processed'
    user = 'root'
    passwd = ''
    host =  'localhost'
    port = 3306
    charset='utf8'
    csv_path = r"./canned_coffee_5star_processed.csv"
    d = DfToMySQL(db=db, host=host, user=user, passwd=passwd, port=port, charset=charset)
    d.set_dataframe(csv_path)    
    d.print_sample_df()
    d.to_mysql(table_name='starbucks_frappuccino_5star')
    # d.execute_query(query='drop table canned_coffee_5star_processed;')


