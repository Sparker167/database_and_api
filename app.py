from flask import Flask, request, jsonify
import pandas as pd
import mysql.connector as connection
from mysql.connector import Error

app = Flask(__name__)



@app.route("/status")
def status():
   return str(1)



@app.route("/getpokemon/<type>", methods=['POST'])
def get_pokemon(type):
   try:
      mydb = connection.connect(host="mysql-db", database = 'myproject',user="datascientest", passwd="root@123",use_pure=True)
      query = f"select * from pokemon where Type1 like '{type}';"
      result_dataFrame = pd.read_sql(query,mydb)
      result_json = result_dataFrame.to_json(orient="index")
      mydb.close() #close the connection
      return result_json
   except Exception as e:
      mydb.close()
      return jsonify({"msg":str(e)})

            


@app.route("/createpokemon", methods=['POST'])
def createpokemon():

   mydb = connection.connect(host="mysql-db", database = 'myproject',user="datascientest", passwd="root@123",use_pure=True)
   data = request.json
   cols = tuple(data.keys())
   values = tuple(data.values())
   part1 = f"INSERT INTO myproject.pokemon {cols} VALUES ".replace("'","") 
   query  = part1+f"{values}"

   cursor = mydb.cursor()
   try:
      cursor.execute(query)
      mydb.commit()
      return jsonify({"msg": 'Pokemon Inserted'})
   except Error as e:
      mydb.close()
      return jsonify({"msg": f"The error '{e}' occurred"})

   


app.run(host='0.0.0.0')
