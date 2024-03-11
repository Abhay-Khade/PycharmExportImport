from sqlalchemy import create_engine
import pandas as pd
import zipfile
import os

db_config = {
    'server': 'ATISL235',
    'database': 'employee2',
    'trusted_connection': 'yes',
    'driver': 'ODBC Driver 17 for SQL Server',
}
engine = create_engine('mssql+pyodbc://' + db_config['server'] +
                       '/' + db_config['database'] +
                       '?trusted_connection=' + db_config['trusted_connection'] +
                       '&driver=' + db_config['driver'])

#file = "D:/Beeline Data_V3 (1).xlsb"
zip_path = 'C:\\Users\\Abhay_Khade\\Downloads\\archive.zip'
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('C:\\Users\\Abhay_Khade\\Downloads\\extracted_files')
files=['artist','canvas_size','image_link','museum','museum_hours','product_size','subject','work']
for file in files:
    file_path = f'C:\\Users\\Abhay_Khade\\Downloads\\extracted_files\\{file}.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.to_sql(file, con=engine, if_exists='replace', index=False)
    else:
        print(f"File not found: {file_path}")



#df = pd.read_excel(file, 'Template', engine='pyxlsb')

# Insert data into the database using SQLAlchemy engine
#df.to_sql('Beeline', con=engine, if_exists='replace', index=False)