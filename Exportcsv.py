from sqlalchemy import create_engine
import pandas as pd

# Database connection configuration
db_config = {
    'server': 'ATISL235',
    'database': 'employee2',
    'trusted_connection': 'yes',
    'driver': 'ODBC Driver 17 for SQL Server',
}

# Create SQLAlchemy engine
engine = create_engine('mssql+pyodbc://' + db_config['server'] +
                       '/' + db_config['database'] +
                       '?trusted_connection=' + db_config['trusted_connection'] +
                       '&driver=' + db_config['driver'])

# Specify the path of the CSV file to be imported
imported_file_path = "D:/exported_data1.csv"

# Read the CSV file into a DataFrame
df_imported = pd.read_csv(imported_file_path)

# Replace NaN values with NULL for proper handling in SQL Server
df_imported = df_imported.where(pd.notna(df_imported), None)

# Specify the table name in the database where you want to import the data
table_name = "exported_data1"

# Import the DataFrame into the SQL Server database table
df_imported.to_sql(table_name, con=engine, if_exists='replace', index=False)

print(f'Data imported to SQL Server table: {table_name}')
