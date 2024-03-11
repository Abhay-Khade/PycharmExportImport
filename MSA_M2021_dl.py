# from sqlalchemy import create_engine
# import pandas as pd
#
# db_config = {
#     'server': 'ATISL235',
#     'database': 'MMM_Imp_Stage',
#     'trusted_connection': 'yes',
#     'driver': 'ODBC Driver 17 for SQL Server',
# }
# engine = create_engine('mssql+pyodbc://' + db_config['server'] +
#                        '/' + db_config['database'] +
#                        '?trusted_connection=' + db_config['trusted_connection'] +
#                        '&driver=' + db_config['driver'])
#
# file = "D:/MSA_M2022_dl.xlsx"
#
# df = pd.read_excel(file, 'MSA_M2022_dl', engine='pyxlsb')
#
# # Insert data into the database using SQLAlchemy engine
# df.to_sql('MSA_M2022_dl', con=engine, if_exists='replace', index=False)

from sqlalchemy import create_engine
import pandas as pd

db_config = {
    'server': 'ATISL235',
    'database': 'MMM_Imp_Stage',
    'trusted_connection': 'yes',
    'driver': 'ODBC Driver 17 for SQL Server',
}
engine = create_engine('mssql+pyodbc://' + db_config['server'] +
                       '/' + db_config['database'] +
                       '?trusted_connection=' + db_config['trusted_connection'] +
                       '&driver=' + db_config['driver'])

file = "D:/MSA_M2022_dl.xlsx"

df = pd.read_excel(file, 'MSA_M2022_dl', engine='pyxlsb')

# Insert data into the database using SQLAlchemy engine
df.to_sql('MSA_M2022_dl', con=engine, if_exists='replace', index=False)