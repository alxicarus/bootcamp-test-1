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
    x=str("'Canada'")
    y=str("'Malaysia'")
    z=str("'Turkey'")

    cursor = conn.cursor()
    sql_3 = 'select "Region", count("Country") as "TotalCountry" from (select "Region" , "Country" from bootcamp_test_alfi group by "Region","Country") as tb2 group by "Region"'
    cursor.execute(sql_3)
    data_3 = cursor.fetchall()
    cursor.close()
    df_3 = pd.DataFrame(data_3, columns=['Region','Total country'])
    print(df_3)

   

    cursor = conn.cursor()
    sql_4 = "select \"Country\" , \"Year\" , max(\"AvgTemperature\"), min(\"AvgTemperature\") from bootcamp_test_alfi where (\"Country\" = 'Canada' or \"Country\" = 'Malaysia' or \"Country\"='Turkey') and \"Year\" = 2018 group by \"Country\", \"Year\" "
    # print(type(sql_4))
    cursor.execute(sql_4)
    data_4 = cursor.fetchall()
    cursor.close()
    df_4 = pd.DataFrame(data_4, columns=['Country','Year','Max temperature','Min Temperature'])
    print(df_4)

    cursor = conn.cursor()
    sql_5 = 'select "Region" ,"Country" , "AvgTemperature" from (select "Region", "Country", "AvgTemperature", "Day", "Month" , "Year" , Rank() over (partition by "Region" order by "AvgTemperature" desc) as rn from bootcamp_test_alfi where "Day" = 1 and "Month" = 10 and "Year" = 2012) as t2 where rn <=5'
    cursor.execute(sql_5)
    data_5 = cursor.fetchall()
    cursor.close()
    df_5 = pd.DataFrame(data_5, columns=['Region','Country','AvgTemperature'])
    print(df_5)



except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit(1) 
print("Connection successful")