import psycopg2
import pandas as pd
import sys

connection_info = {
    "host"      : "206.189.80.195",
    "database"  : "bootcamp",
    "user"      : "bootcamp",
    "password"  : "Bootcamp*123"
}
conn = None

try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**connection_info)
    
    cursor = conn.cursor()
    sql_3 = 'select "Region", "Country", "AvgTemperature" from (select "Region","Country" , "AvgTemperature", rank ()over (partition by "Country" order by "AvgTemperature" desc) as rn from bootcamp_test_alfi where "AvgTemperature" >100) as t2 where rn = 1 order by "Region" asc, "Country" asc'
    cursor.execute(sql_3)
    data_3 = cursor.fetchall()
    cursor.close()
    df_3 = pd.DataFrame(data_3, columns=['Region','country','Max Temp'])
    print(df_3)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit(1) 
print("Connection successful")