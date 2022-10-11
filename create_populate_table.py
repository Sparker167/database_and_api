import pandas as pd
import mysql.connector as connection
from mysql.connector import Error
import sys

pokemondf = pd.read_csv("Pokemon.csv", sep=",")

try:
    conn = connection.connect(host="mysql-db", database = 'myproject',user="datascientest", passwd="root@123",use_pure=True)
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS pokemon;')
        print('Creating table....')
        # Create Table
        cursor.execute("CREATE TABLE myproject.pokemon(Num varchar(25), Name varchar(255), Type1 varchar(25), Type2 varchar(25), Total varchar(255), HP INT, Attack INT, Defense INT, SpAtk INT, SpDef INT, Speed INT, Generation INT, Legendary varchar(255))")
        print("Table is created....")
        
        #loop through the data frame
        for i,row in pokemondf.iterrows():
            #here %S means string values 
            sql = "INSERT INTO myproject.pokemon VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)
            sys.exit(1)